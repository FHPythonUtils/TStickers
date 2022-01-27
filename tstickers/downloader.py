"""Sticker download functions used by the module entry point."""

from __future__ import annotations

import os
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from json.decoder import JSONDecodeError
from sys import exit as sysexit
from typing import Any

from emoji import demojize

from . import caching
from .convert import convertAnimated, convertStatic

opj = os.path.join


def assureDirExists(directory: str, root: str) -> str:
	"""make the dir if not exists

	Args:
		directory (str): the directory name
		root (str): the path of the root directory

	Returns:
		str: the full path
	"""
	fullPath = opj(root, directory)
	if os.path.isdir(fullPath):
		pass
	else:
		os.mkdir(fullPath)

	return fullPath


class Sticker:
	"""Sticker instance attributes"""

	def __init__(
		self, name: str = "None", link: str = "None", emoji: str = "😀", animated: bool = False
	):
		self.name = name
		self.link = link
		self.emoji = emoji
		self.animated = animated

	def __repr__(self):
		return f"<Sticker:{self.name}>"

	def emojiName(self) -> str:
		"""get the emoji as a string"""
		return demojize(self.emoji)[1:-1]


class StickerDownloader:
	"""The StickerDownloader sets up the api and makes requests"""

	def __init__(self, token, session=None, multithreading=4):
		self.threads = multithreading
		self.token = token
		self.cwd = assureDirExists("downloads", root=os.getcwd())
		if session is None:
			self.session = caching.cachedSession
		else:
			self.session = session
		self.api = f"https://api.telegram.org/bot{self.token}/"
		verify = self.doAPIReq("getMe", {})
		if verify is not None and verify["ok"]:
			pass
		else:
			print("Invalid token.")
			sysexit(1)

	def doAPIReq(self, function: str, params: dict[Any, Any]) -> dict[Any, Any] | None:
		"""Use the telegram api

		Args:
			function (str): function to execute
			params (dict[Any, Any]): function parameters

		Raises:
			RuntimeError: In the event of a failure

		Returns:
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

		print(f'API method {function} with params {params} failed. Error: "{res["description"]}"')
		return None

	def getSticker(self, fileData: dict[Any, Any]) -> Sticker:
		"""Get sticker info from the server

		Args:
			fileData (dict[Any, Any]): sticker id

		Returns:
			Sticker: Sticker instance
		"""
		info = self.doAPIReq("getFile", {"file_id": fileData["file_id"]})
		if info is not None:
			file = Sticker(
				name=info["result"]["file_path"].split("/")[-1],
				link=f'https://api.telegram.org/file/bot{self.token}/{info["result"]["file_path"]}',
				emoji=fileData["emoji"],
				animated=fileData["is_animated"],
			)
			return file
		return Sticker()

	def getPack(self, packName: str) -> dict[str, Any] | None:
		"""Get a list of File objects.

		Args:
			packName (str): name of the pack

		Returns:
			dict[str, Any]: dictionary containing sticker data
		"""
		params = {"name": packName}
		res = self.doAPIReq("getStickerSet", params)
		if res is None:
			return None
		stickers = res["result"]["stickers"]
		files = []

		print(f'Starting to scrape "{packName}" ..')
		start = time.time()
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			futures = [executor.submit(self.getSticker, i) for i in stickers]
			for i in as_completed(futures):
				files.append(i.result())
		end = time.time()
		print(f"Time taken to scrape {len(files)} stickers - {end - start:.3f}s")
		print()

		pack = {
			"name": res["result"]["name"].lower(),
			"title": res["result"]["title"],
			"files": files,
		}
		return pack

	def downloadSticker(self, name: str, link: str, path: str) -> str:
		"""Download a sticker from the server.

		Args:
			name (str): the name of the file
			link (str): the url to the file on the server
			path (str): the path to write to

		Returns:
			str: the filepath the file is written to
		"""
		filePath = opj(path, name)
		with open(filePath, "wb") as file:
			res = self.session.get(link)
			file.write(res.content)
		return filePath

	def downloadPack(self, pack: dict[str, Any]) -> list[str]:
		"""Download a sticker pack.

		Args:
			pack (dict[str, Any]): dictionary representing a sticker pack

		Returns:
			list[str]: list of file paths each sticker is written to
		"""
		swd = assureDirExists(pack["name"], root=self.cwd)
		webpDir = assureDirExists("webp", root=swd)
		tgsDir = assureDirExists("tgs", root=swd)
		downloads = []

		print(f'Starting download of "{pack["name"]}" into {swd}')
		start = time.time()
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			futures = [
				executor.submit(
					self.downloadSticker,
					name=(
						f'{sticker.name.split("_")[-1].split(".")[0]}+{sticker.emojiName()}'
						f'.{("tgs" if sticker.animated else "webp")}'
					),
					link=sticker.link,
					path=tgsDir if sticker.animated else webpDir,
				)
				for sticker in pack["files"]
			]
			for i in as_completed(futures):
				downloads.append(i.result())
		self.session.close()

		end = time.time()
		print(f"Time taken to download {len(downloads)} stickers - {end - start:.3f}s")
		print()
		return downloads

	def convertPack(self, packName: str, frameSkip: int = 1, scale: float = 1, noCache=False):
		"""Convert the webp to gif and png; tgs to gif, webp (webp_animated) and png.

		Args:
			packName (str): name of the directory to convert
			frameSkip (int, optional): skip n number of frames in the interest of
			optimisation with a quality trade-off. Defaults to 1.
			scale (float, optional): upscale/ downscale the images produced. Intended
			for optimisation with a quality trade-off. Defaults to 1.
			noCache (bool, optional): set to true to disable cache. Defaults to False.
		"""
		if not noCache and caching.verifyConverted(packName):
			return
		# Make directories
		swd = assureDirExists(packName, root=self.cwd)
		assureDirExists("webp_animated", root=swd)
		assureDirExists("png", root=swd)
		assureDirExists("gif", root=swd)

		# Convert Stickers
		start = time.time()
		print(f'Converting stickers "{packName}"...')
		total = len(
			os.listdir(opj(swd, "webp"))
			+ [i for i in os.listdir(opj(swd, "tgs")) if i.endswith(".tgs")]
		)
		# 	Static
		converted = convertedStatic = convertStatic(swd, self.threads)

		# 	Animated
		convertedAnimated = convertAnimated(swd, self.threads, frameSkip=frameSkip, scale=scale)
		converted += convertedAnimated

		end = time.time()
		print(f"Time taken to convert {converted}/{total} stickers (total) - {end - start:.3f}s")
		print()

		caching.createConverted(
			packName,
			data={
				"version": 1,
				"info": {
					"packName": packName,
					"frameSkip": frameSkip,
					"scale": scale,
					"swd": swd,
				},
				"converted": {
					"static": convertedStatic,
					"animated": convertedAnimated,
					"total": total,
				},
			},
		)
