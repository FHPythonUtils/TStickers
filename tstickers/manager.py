"""Sticker download functions used by the module entry point."""

from __future__ import annotations

import re
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from json.decoder import JSONDecodeError
from pathlib import Path
from sys import exit as sysexit
from typing import Any

from emoji import EMOJI_DATA
from loguru import logger

from tstickers import caching
from tstickers.convert import Backend, convertAnimated, convertStatic


def demojize(emoji: str) -> str:
	"""Similar to the emoji.demojize function.

	However, returns a string of unique keywords in alphabetical order seperated by "_"

	:param str emoji: emoji unicode char
	:return str: returns a string of unique keywords in alphabetical order seperated by "_"
	"""

	def c14n_part(part: str) -> str:
		return re.sub(r"_!@#$%^&*'", "_", part).replace("-", "_").lower()

	def merge_parts(parts: set[str]) -> str:
		unique_set = set()
		for part in parts:
			unique_set.update(part.split("_"))

		unique_set.discard("")
		unique_set.discard("with")

		result_list = sorted(unique_set)
		return "_".join(result_list)

	emoji_data = EMOJI_DATA.get(emoji)
	if emoji_data is None:
		return "unknown"

	parts = {c14n_part(emoji_data.get("en", "").strip(":"))}
	parts.update(c14n_part(x.strip(":")) for x in emoji_data.get("alias", []))

	return merge_parts(parts)


@dataclass
class Sticker:
	"""Sticker instance attributes."""

	name: str = "None"
	link: str = "None"
	emoji: str = "😀"
	fileType: str = "webp"

	def __repr__(self) -> str:
		"""Get Sticker representation in the form <Sticker:name>.

		:return str: representation
		"""
		return f"<Sticker:{self.name}>"

	def emojiName(self) -> str:
		"""Get the emoji as a string."""
		return demojize(self.emoji)


class StickerManager:
	"""The StickerManager sets up the api and makes requests."""

	def __init__(
		self,
		token: str,
		session: caching.CachedSession | None = None,
		threads: int = 4,
	) -> None:
		"""Telegram Sticker API and provides functions to simplify downloading
		new packs.

		:param str token: bot token obtained from @BotFather
		:param caching.CachedSession | None session: the requests session to use, defaults to None
		:param int threads: number of threads to download over, defaults to 4
		"""
		self.threads = threads
		self.token = token
		self.cwd = Path("downloads")
		if session is None:
			self.session = caching.cachedSession
		else:
			self.session = session
		self.api = f"https://api.telegram.org/bot{self.token}/"
		verify = self.doAPIReq("getMe", {})
		if verify is not None and verify["ok"]:
			pass
		else:
			logger.info("Invalid token.")
			sysexit(1)

	def doAPIReq(self, function: str, params: dict[Any, Any]) -> dict[Any, Any] | None:
		"""Use the telegram api.

		Args:
		----
			function (str): function to execute
			params (dict[Any, Any]): function parameters

		Raises:
		------
			RuntimeError: In the event of a failure

		Returns:
		-------
			Optional[dict[Any, Any]]: api response

		"""
		urlParams = "?" + urllib.parse.urlencode(params)
		res = self.session.get(f"{self.api}{function}{urlParams}")
		try:
			res = res.json()
		except JSONDecodeError:
			res = {"ok": False, "raw": res}
		if res["ok"]:
			return res

		logger.info(
			f'API method {function} with params {params} failed. Error: "{res["description"]}"'
		)
		return None

	def getSticker(self, fileData: dict[str, Any]) -> Sticker:
		"""Get sticker info from the server.

		Args:
		----
			fileData (dict[str, Any]): sticker id

		Returns:
		-------
			Sticker: Sticker instance

		"""
		info = self.doAPIReq("getFile", {"file_id": fileData["file_id"]})
		if info is not None:
			filePath = info["result"]["file_path"]
			return Sticker(
				name=filePath.split("/")[-1],
				link=f"https://api.telegram.org/file/bot{self.token}/{filePath}",
				emoji=fileData["emoji"],
				fileType=filePath.split(".")[-1],
			)
		return Sticker()

	def getPack(self, packName: str) -> dict[str, Any] | None:
		"""Get a list of File objects.

		Args:
		----
			packName (str): name of the pack

		Returns:
		-------
			dict[str, Any]: dictionary containing sticker data

		"""
		params = {"name": packName}
		res = self.doAPIReq("getStickerSet", params)
		if res is None:
			return None
		stickers = res["result"]["stickers"]
		files = []

		logger.info(f'Starting to scrape "{packName}" ..')
		start = time.time()
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			futures = [executor.submit(self.getSticker, i) for i in stickers]
			files = [i.result() for i in as_completed(futures)]
		end = time.time()
		logger.info(f"Time taken to scrape {len(files)} stickers - {end - start:.3f}s")
		logger.info("")

		return {
			"name": res["result"]["name"].lower(),
			"title": res["result"]["title"],
			"files": files,
		}

	def downloadSticker(self, path: Path, link: str) -> int:
		"""Download a sticker from the server.

		:param Path path: the path to write to
		:param str link: the url to the file on the server

		:return int: path.write_bytes(res.content)

		"""
		path.parent.mkdir(parents=True, exist_ok=True)
		return path.write_bytes(self.session.get(link).content)

	def downloadPack(self, packName: str) -> bool:
		"""Download a sticker pack.

		:param str packName: name of the pack
		:return bool: success

		"""

		stickerPack = self.getPack(packName)
		if stickerPack is None:
			return False

		swd: Path = self.cwd / packName
		swd.mkdir(parents=True, exist_ok=True)

		downloads = 0
		logger.info(f'Starting download of "{packName}" into {swd}')
		start = time.time()
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			futures = [
				executor.submit(
					self.downloadSticker,
					swd
					/ sticker.fileType
					/ (
						f"{sticker.name.split('_')[-1].split('.')[0]}+{sticker.emojiName()}"
						f".{sticker.fileType}"
					),
					link=sticker.link,
				)
				for sticker in stickerPack["files"]
			]
			for i in as_completed(futures):
				downloads += 1 if i.result() > 0 else 0
		self.session.close()

		end = time.time()
		logger.info(f"Time taken to download {downloads} stickers - {end - start:.3f}s")
		logger.info("")
		return downloads == stickerPack["files"]

	def convertPack(
		self,
		packName: str,
		fps: int = 20,
		scale: float = 1,
		*,
		noCache: bool = False,
		backend: Backend = Backend.UNDEFINED,
		formats: set[str] | None = None,
	) -> None:
		"""Convert a downloaded sticker pack given by packName to other formats specified.

		:param str packName: name of the pack to convert
		:param int fps: framerate of animated stickers, affecting optimization and
		quality (default: 20)
		:param float scale: Scale factor of animated stickers, for up/downscaling images,
		affecting optimization and quality (default: 1).
		:param bool noCache: set to true to disable cache. Defaults to False.
		:param Backend backend: select the backend to use to convert animated stickers
		:param set[str]|None formats: Set of formats to convert telegram tgs stickers to
		(default: {"gif", "webp", "apng"})

		"""
		if formats is None:
			formats = {"gif", "png", "webp", "apng"}
		if not noCache and caching.verify_converted(packName):
			return
		swd = self.cwd / packName

		start = time.time()
		total = len([x for x in swd.glob("**/*") if x.is_file()])

		logger.info(f'Converting stickers "{packName}"...')

		for fmt in formats:
			(swd / fmt).mkdir(parents=True, exist_ok=True)

		animatedFormats = formats.copy()
		animatedFormats.discard("png")

		converted = convertedTgs = convertAnimated(
			swd, self.threads, fps=fps, scale=scale, backend=backend, formats=animatedFormats
		)

		convertedWebp = convertStatic(swd, self.threads, formats=formats)
		converted += convertedWebp

		end = time.time()
		logger.info(f"Time taken to convert {converted} stickers (total) - {end - start:.3f}s")
		logger.info("")

		caching.create_converted(
			packName,
			data={
				"version": 2,
				"info": {
					"packName": packName,
					"fps": fps,
					"scale": scale,
					"swd": swd.as_posix(),
				},
				"converted": {
					"static": convertedWebp,
					"animated": convertedTgs,
					"total": total,
				},
			},
		)
