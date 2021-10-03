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


def ls(directory: str) -> list[str]:
	"""Do an ls

	Args:
		directory (str): directory to ls

	Returns:
		list[str]: list of file paths
	"""
	return [opj(directory, i) for i in os.listdir(directory)]


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
					name=(
						f'{sticker.name.split("_")[-1].split(".")[0]}+{sticker.emojiName()}'
						f'.{("tgs" if sticker.animated else "webp")}'
					),
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

	def convertWithPIL(self, swd: str, srcDir: str, inputFile: str, static: bool = True) -> str:
		"""Convert the webp file to png

		Args:
			swd (str): sticker working directory
			srcDir (str): sticker src directory
			inputFile (str): path to input file
			static (bool): for static stickers

		Returns:
			str: path to input file
		"""
		img = Image.open(inputFile)
		img.save(inputFile.replace(srcDir, opj(swd, "png")).replace("webp", "png"))

		if static:
			try:
				img.save(inputFile.replace(srcDir, opj(swd, "gif")).replace("webp", "gif"))
			except ValueError:
				print(f"Failed to save {inputFile} as gif")
		return inputFile

	def convertDir(self, packName: str, frameSkip: int = 1, scale: float = 1):
		"""Convert the webp images into png images

		Args:
			packName (str): name of the directory to convert
			frameSkip (int, optional): skip n number of frames in the interest of
			optimisation with a quality trade-off. Defaults to 1.
			scale (float, optional): upscale/ downscale the images produced. Intended
			for optimisation with a quality trade-off. Defaults to 1.
		"""
		# Make directories
		swd = assureDirExists(packName, root=self.cwd)
		webpDir = assureDirExists("webp", root=swd)
		tgsDir = assureDirExists("tgs", root=swd)
		webpAnimatedDir = assureDirExists("webp_animated", root=swd)
		assureDirExists("png", root=swd)
		assureDirExists("gif", root=swd)

		# Convert Stickers
		print(f'Converting stickers "{packName}"...')
		converted = 0
		start = time.time()

		# 	Static
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			for _ in as_completed(
				[
					executor.submit(self.convertWithPIL, swd, webpDir, inputFile)
					for inputFile in ls(webpDir)
				]
			):
				converted += 1

		# 	Animated
		doConvMultLottie = (
			lambda fm, fs, sc: len(
				asyncio.run(pyrlottie.convMultLottie(fm, frameSkip=fs, scale=sc))
			)
			// 2
		)
		converted += doConvMultLottie(
			fm=[
				pyrlottie.FileMap(
					pyrlottie.LottieFile(stckr),
					{
						stckr.replace(tgsDir, opj(swd, "gif")).replace("tgs", "gif"),
						stckr.replace(tgsDir, webpAnimatedDir).replace("tgs", "webp"),
					},
				)
				for stckr in [i for i in ls(tgsDir) if i.endswith(".tgs")]
			],
			fs=frameSkip,
			sc=scale,
		)
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			for _ in as_completed(
				[
					executor.submit(self.convertWithPIL, swd, webpAnimatedDir, inputFile, False)
					for inputFile in ls(webpAnimatedDir)
				]
			):
				_.result()

		end = time.time()
		print(f"Time taken to convert {converted} stickers - {end - start:.3f}s")
		print()
