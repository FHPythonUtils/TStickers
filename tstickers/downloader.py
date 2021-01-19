from __future__ import annotations
"""Provides the module functions
"""
import json
from typing import Any, Optional
import urllib.parse
from concurrent.futures import as_completed, ThreadPoolExecutor
from sys import exit as sysexit
import time
import os
import shutil
import requests
from PIL import Image
from emoji import demojize
import pylottie

opj = os.path.join


def assureDirExists(directory: str, root: str) -> str:
	"""make the dir if not exists

	Args:
		dir (str): the directory name
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
	"""Sticker instance attributes
	"""
	def __init__(self, name: str = "None", link: str = "None", emoji: str = "😀",
	animated: bool = False):
		self.name = name
		self.link = link
		self.emoji = emoji
		self.animated = animated

	def __repr__(self):
		return "<F:{}>".format(self.name)

	def emojiName(self) -> str:
		""" get the emoji as a string """
		return demojize(self.emoji)[1:-1]


class StickerDownloader:
	"""The StickerDownloader sets up the api and makes requests
	"""
	def __init__(self, token, session=None, multithreading=4):
		self.threads = multithreading
		self.token = token
		self.cwd = assureDirExists("downloads", root=os.getcwd())
		if session is None:
			self.session = requests.Session()
		else:
			self.session = session
		self.api = "https://api.telegram.org/bot{}/".format(self.token)
		verify = self.doAPIReq("getMe", {})
		if verify is not None and verify["ok"]:
			pass
		else:
			print("Invalid token.")
			sysexit()

	def doAPIReq(self, fstring: str, params: dict[Any, Any]) -> Optional[dict[Any,
	Any]]:
		"""Use the telegram api

		Args:
			fstring (str): function to execute
			params (dict[Any, Any]): function parameters

		Raises:
			RuntimeError: In the event of a failure

		Returns:
			Optional[dict[Any, Any]]: api response
		"""
		try:
			urlParams = "?" + urllib.parse.urlencode(params)
			res = self.session.get("{}{}{}".format(self.api, fstring, urlParams))
			if res.status_code != 200:
				raise RuntimeError
			res = json.loads(res.content.decode("utf-8"))
			if not res["ok"]:
				raise RuntimeError(res["description"])
			return res
		except RuntimeError as exception:
			print("API method {} failed. Error: \"{}\"".format(fstring, exception))
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
			link="https://api.telegram.org/file/bot{}/{}"
			.format(self.token, info["result"]["file_path"]), emoji=fileData["emoji"],
			animated=fileData["is_animated"])
			return file
		return Sticker()

	def getStickerSet(self, name: str) -> Optional[dict[Any, Any]]:
		"""	Get a list of File objects.

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

		print("Starting to scrape \"{}\" ..".format(name))
		start = time.time()
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			futures = [executor.submit(self.getSticker, i) for i in stickers]
			for i in as_completed(futures):
				files.append(i.result())
		end = time.time()
		print("Time taken to scrape {} stickers - {:.3f}s"
		.format(len(files), end - start))
		print()

		stickerSet = {
		"name": res["result"]["name"].lower(), "title": res["result"]["title"],
		"files": files}
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

		print("Starting download of \"{}\" into {}".format(stickerSet["name"], swd))
		start = time.time()
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			futures = [executor.submit(self.downloadSticker,
			name="{}+{}+{}.{}".format(sticker.name.split("_")[-1].split(".")[0],
			sticker.emojiName(), sticker.emoji,
			("tgs" if sticker.animated else "webp")),
			link=sticker.link,
			path=tgsDir if sticker.animated else webpDir)
			for sticker in stickerSet["files"]] # yapf: disable
			for i in as_completed(futures):
				downloads.append(i.result())

		end = time.time()
		print("Time taken to download {} stickers - {:.3f}s"
		.format(len(downloads), end - start))
		print()
		return downloads

	def convertStatic(self, inputFile: str):
		"""Convert the webp file to png

		Args:
			inputFile (str): path to input file

		Returns:
			None
		"""
		img = Image.open(inputFile)
		img.save(inputFile.replace("webp", "png"))
		try:
			img.save(inputFile.replace("webp", "gif"), transparency=0,
			save_all=True, optimize=False) # yapf: disable
		except ValueError:
			print("Failed to save {} as gif".format(inputFile))

	def convertDir(self, name: str, quality: int = 1):
		"""	Convert the webp images into png images

		Args:
			name (str): name of the directory to convert
			quality (int): quality of animated images. Default=1
		"""
		# yapf: disable
		# Make directories
		swd = assureDirExists(name, root=self.cwd)
		webpDir = assureDirExists("webp", root=swd)
		tgsDir = assureDirExists("tgs", root=swd)
		assureDirExists("png", root=swd)
		assureDirExists("gif", root=swd)
		# List of animated stickers
		animatedStickers = [opj(tgsDir, i) for i in os.listdir(tgsDir)
		if i.endswith(".tgs")]
		# List of static stickers
		staticStickers = [opj(webpDir, i) for i in os.listdir(webpDir)]
		# Convert Stickers
		print("Converting stickers \"{}\"...".format(name))
		converted = 0
		start = time.time()
		# 	Static
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			futures = [executor.submit(self.convertStatic, inputFile)
			for inputFile in staticStickers]
			for _i in as_completed(futures):
				converted += 1
		# 	Animated
		if len(animatedStickers) > 0:
			imageDataList = pylottie.convertLotties2PIL(animatedStickers, quality)
			for index, imageData in enumerate(imageDataList):
				images = imageData[0]
				duration = imageData[1]
				converted += 1
				images[0].save(animatedStickers[index].replace("tgs", "gif"), save_all=True, append_images=images[1:],
				duration=duration*1000/len(images), loop=0, transparency=0, disposal=2)
				images[0].save(animatedStickers[index].replace("tgs", "webp"), save_all=True, append_images=images[1:],
				duration=int(duration*1000/len(images)), loop=0)
			shutil.rmtree("temp", ignore_errors=True)
		end = time.time()
		print("Time taken to convert {} stickers - {:.3f}s".format(converted, end - start))
		print()
		# yapf: enable
