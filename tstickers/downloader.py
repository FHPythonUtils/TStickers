from __future__ import annotations
"""Provides the module functions
"""
import json
from typing import Any, Optional
import urllib.parse
from shutil import copy
from concurrent.futures import as_completed, ThreadPoolExecutor
from sys import exit as sysexit
import time
import os
import requests
from PIL import Image
import tstickers.animate as animate


def assureDirExists(directory: str, root: str) -> str:
	"""make the dir if not exists

	Args:
		dir (str): the directory name
		root (str): the path of the root directory

	Returns:
		str: the full path
	"""
	fullPath = os.path.join(root, directory)
	if os.path.isdir(fullPath):
		pass
	else:
		os.mkdir(fullPath)

	return fullPath


class File:
	"""File container has name and a link
	"""
	def __init__(self, name: str, link: str):
		self.name = name
		self.link = link

	def __repr__(self):
		return '<F:{}>'.format(self.name)


class StickerDownloader:
	"""The StickerDownloader sets up the api and makes requests
	"""
	def __init__(self, token, session=None, multithreading=4):
		self.threads = multithreading
		self.token = token
		self.cwd = assureDirExists('downloads', root=os.getcwd())
		assureDirExists('temp', root=os.getcwd())
		if session is None:
			self.session = requests.Session()
		else:
			self.session = session
		self.api = 'https://api.telegram.org/bot{}/'.format(self.token)
		verify = self.doAPIReq('getMe', {})
		if verify is not None and verify['ok']:
			pass
		else:
			print('Invalid token.')
			sysexit()

	def doAPIReq(self, fstring: str, params: dict[Any, Any]) -> Optional[dict[Any,
	Any]]:
		'''
		general method call
		'''
		try:
			urlParams = '?' + urllib.parse.urlencode(params)

			res = self.session.get('{}{}{}'.format(self.api, fstring, urlParams))
			if res.status_code != 200:
				raise RuntimeError

			res = json.loads(res.content.decode('utf-8'))
			if not res['ok']:
				raise RuntimeError(res['description'])

			return res

		except RuntimeError as exception:
			print('API method {} failed. Error: "{}"'.format(fstring, exception))
			return None

	def getFile(self, fileId: str) -> File:
		"""Get the file from the server

		Args:
			fileId (str): sticker id

		Returns:
			File: [description]
		"""
		info = self.doAPIReq('getFile', {'file_id': fileId})
		if info is not None:
			file = File(
			name=info['result']['file_path'].split('/')[-1],
			link='https://api.telegram.org/file/bot{}/{}'
			.format(self.token, info['result']['file_path']))

			return file
		return File("Err", "Err")

	def getStickerSet(self, name: str) -> Optional[dict[Any, Any]]:
		"""	Get a list of File objects.

		Args:
			name (str): name of the sticker set

		Returns:
			dict[Any, Any]: dictionary containing sticker data
		"""
		params = {'name': name}
		res = self.doAPIReq('getStickerSet', params)
		if res is None:
			return None

		stickers = res['result']['stickers']
		files = []

		print('Starting to scrape "{}" ..'.format(name))
		start = time.time()

		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			futures = [executor.submit(self.getFile, i['file_id']) for i in stickers]
			for i in as_completed(futures):
				files.append(i.result())

		end = time.time()

		print('Time taken to scrape {} stickers - {:.3f}s'
		.format(len(files), end - start))
		print()

		stickerSet = {
		'name': res['result']['name'].lower(), 'title': res['result']['title'],
		'files': files}

		return stickerSet

	def downloadFile(self, name: str, link: str, path: str) -> str:
		"""Download a file from the server

		Args:
			name (str): the name of the file
			link (str): the url to the file on the server
			path (str): the path

		Returns:
			str: the filepath the file was written to
		"""
		filePath = os.path.join(path, name)
		with open(filePath, 'wb') as file:
			res = self.session.get(link)
			file.write(res.content)
		return filePath

	def downloadStickerSet(self, stickerSet: dict[Any, Any]):
		'''
		Download sticker set.
		'''
		swd = assureDirExists(stickerSet['name'], root=self.cwd)
		downloadPath = assureDirExists('input', root=swd)
		downloads = []

		print('Starting download of "{}" into {}'.format(stickerSet['name'],
		downloadPath))
		start = time.time()
		with ThreadPoolExecutor(max_workers=self.threads) as executor:
			futures = [
			executor.submit(self.downloadFile, f.name, f.link, downloadPath)
			for f in stickerSet['files']]
			for i in as_completed(futures):
				downloads.append(i.result())

		end = time.time()
		print('Time taken to download {} stickers - {:.3f}s'
		.format(len(downloads), end - start))
		print()

		return downloads

	def convertImg(self, inputFile: str):
		"""Convert the webp file to png

		Args:
			inputFile (str): path to input file

		Returns:
			None
		"""
		if inputFile.endswith(".webp"):
			img = Image.open(inputFile)
			img.save(inputFile.replace("input", "webp"))
			img.save(inputFile.replace("webp", "png").replace("input", "png"))
			try:
				img.save(
				inputFile.replace("webp", "gif").replace("input", "gif"), transparency=0)
			except ValueError:
				print("Failed to save {} as gif".format(inputFile))
		else:
			copy(inputFile, inputFile.replace("input", "tgs"))
			images, duration = animate.convertTGS2PIL(inputFile)
			animate.convertTGS2GIF(
			images, duration,
			inputFile.replace("tgs", "gif").replace("input", "gif"))
			animate.convertTGS2Webp(
			images, duration,
			inputFile.replace("tgs", "webp").replace("input", "webp"))

	def convertDir(self, name: str):
		"""	Convert the webp images into png images

		Args:
			name (str): name of the directory to convert
		"""
		swd = assureDirExists(name, root=self.cwd)
		inputDir = assureDirExists('input', root=swd)
		assureDirExists('png', root=swd)
		assureDirExists('gif', root=swd)
		assureDirExists('webp', root=swd)
		assureDirExists('tgs', root=swd)
		inputFiles = [os.path.join(inputDir, i) for i in os.listdir(inputDir)]
		pngFiles = []

		print('Converting stickers "{}"..'.format(name))
		start = time.time()

		pngFiles = [self.convertImg(inputFile) for inputFile in inputFiles]

		end = time.time()
		print('Time taken to convert {} stickers - {:.3f}s'
		.format(len(pngFiles), end - start))
		print()
