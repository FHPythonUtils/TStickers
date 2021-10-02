"""Provides the module functions
"""
from __future__ import annotations

import asyncio
import json
import os
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from sys import exit as sysexit
from typing import Any, Optional

import pyrlottie
import requests
from emoji import demojize
from PIL import Image

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
			self.session = requests.Session()
		else:
			self.session = session
		self.api = f"https://api.telegram.org/bot{self.token}/"
		verify = self.doAPIReq("getMe", {})
		if verify is not None and verify["ok"]:
			pass
		else:
			print("Invalid token.")
			sysexit()

	def doAPIReq(self, function: str, params: dict[Any, Any]) -> Optional[dict[Any, Any]]:
		"""Use the telegram api

		Args:
			function (str): function to execute
			params (dict[Any, Any]): function parameters

		Raises:
			RuntimeError: In the event of a failure

		Returns:
			Optional[dict[Any, Any]]: api response
		"""
		try:
			urlParams = "?" + urllib.parse.urlencode(params)
			res = self.session.get(f"{self.api}{function}{urlParams}")
			if res.status_code != 200:
				raise RuntimeError
			res = json.loads(res.content.decode("utf-8"))
			if not res["ok"]:
				raise RuntimeError(res["description"])
			return res
		except RuntimeError as exception:
			print(f'API method {function} failed. Error: "{exception}"')
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

	def getStickerSet(self, name: str) -> Optional[dict[Any, Any]]:
		"""Get a list of File objects.

		Args:
			name (str): name of the sticker set

		Returns:
			dict[Any, Any]: dictionary containing sticker data
		"""
		params = {"name": name}
		res = self.doAPIReq("getStickerSet", params)
		if res is None:
			return None
		stickers = res["result"]["stickers"]
		files = []

		print(f'Starting to scrape "{name}" ..')
		start = time.time()
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			futures = [executor.submit(self.getSticker, i) for i in stickers]
			for i in as_completed(futures):
				files.append(i.result())
		end = time.time()
		print(f"Time taken to scrape {len(files)} stickers - {end - start:.3f}s")
		print()

		stickerSet = {
			"name": res["result"]["name"].lower(),
			"title": res["result"]["title"],
			"files": files,
		}
		return stickerSet

	def downloadSticker(self, name: str, link: str, path: str) -> str:
		"""Download a sticker from the server

		Args:
			name (str): the name of the file
			link (str): the url to the file on the server
			path (str): the path to write to

		Returns:
			str: the filepath the file was written to
		"""
		filePath = opj(path, name)
		with open(filePath, "wb") as file:
			res = self.session.get(link)
			file.write(res.content)
		return filePath

	def downloadStickerSet(self, stickerSet: dict[Any, Any]):
		"""
		Download sticker set.
		"""
		swd = assureDirExists(stickerSet["name"], root=self.cwd)
		webpDir = assureDirExists("webp", root=swd)
		tgsDir = assureDirExists("tgs", root=swd)
		downloads = []

		print(f'Starting download of "{stickerSet["name"]}" into {swd}')
		start = time.time()
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			futures = [
				executor.submit(
					self.downloadSticker,
					name=f'{sticker.name.split("_")[-1].split(".")[0]}+{sticker.emojiName()}.{("tgs" if sticker.animated else "webp")}',
					link=sticker.link,
					path=tgsDir if sticker.animated else webpDir,
				)
				for sticker in stickerSet["files"]
			]
			for i in as_completed(futures):
				downloads.append(i.result())
		self.session.close()

		end = time.time()
		print(f"Time taken to download {len(downloads)} stickers - {end - start:.3f}s")
		print()
		return downloads

	def convertStatic(self, inputFile: str):
		"""Convert the webp file to png

		Args:
			inputFile (str): path to input file

		"""
		img = Image.open(inputFile)
		img.save(inputFile.replace("webp", "png"))

		try:
			img.save(
				inputFile.replace("webp", "gif"), transparency=0, save_all=True, optimize=False
			)
		except ValueError:
			print(f"Failed to save {inputFile} as gif")

	def convertDir(self, name: str, frameSkip: int = 1, scale: float = 1):
		"""Convert the webp images into png images

		Args:
			name (str): name of the directory to convert
			frameSkip (int, optional): skip n number of frames in the interest of
			optimisation with a quality trade-off. Defaults to 1.
			scale (float, optional): upscale/ downscale the images produced. Intended
			for optimisation with a quality trade-off. Defaults to 1.
		"""
		# Make directories
		swd = assureDirExists(name, root=self.cwd)
		webpDir = assureDirExists("webp", root=swd)
		tgsDir = assureDirExists("tgs", root=swd)
		assureDirExists("png", root=swd)
		assureDirExists("gif", root=swd)
		# List of animated stickers
		animatedStickers = [opj(tgsDir, i) for i in os.listdir(tgsDir) if i.endswith(".tgs")]
		# List of static stickers
		staticStickers = [opj(webpDir, i) for i in os.listdir(webpDir)]
		# Convert Stickers
		print(f'Converting stickers "{name}"...')
		converted = 0
		start = time.time()
		# 	Static
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			futures = [
				executor.submit(self.convertStatic, inputFile) for inputFile in staticStickers
			]
			for _ in as_completed(futures):
				converted += 1
		# 	Animated
		if len(animatedStickers) > 0:
			converted += int(
				len(
					asyncio.run(
						pyrlottie.convMultLottie(
							[
								pyrlottie.FileMap(
									pyrlottie.LottieFile(animatedSticker),
									{
										animatedSticker.replace("tgs", "gif"),
										animatedSticker.replace("tgs", "webp"),
									},
								)
								for animatedSticker in animatedStickers
							],
							frameSkip=frameSkip,
							scale=scale,
						)
					)
				)
				/ 2
			)
		end = time.time()
		print(f"Time taken to convert {converted} stickers - {end - start:.3f}s")
		print()
