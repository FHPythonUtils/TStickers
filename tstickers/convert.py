"""Sticker convert functions used by the downloader."""
import asyncio
import os
import os.path
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import pyrlottie
from PIL import Image

opj = os.path.join


def ls(directory: str) -> list[str]:  # pylint: disable=invalid-name
	"""Do an ls

	Args:
		directory (str): directory to ls

	Returns:
		list[str]: list of file paths
	"""
	return [opj(directory, i) for i in os.listdir(directory)]


def convertWithPIL(swd: str, srcDir: str, inputFile: str, static: bool = True) -> str:
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


def convertStatic(swd: str, threads: int = 4) -> int:
	"""Convert static stickers to png and gif

	Args:
		swd (str): the sticker working directory (downloads/packName)
		threads (int, optional): number of threads to pass to ThreadPoolExecutor. Defaults to 4.

	Returns:
		int: number of stickers successfully converted
	"""
	converted = 0
	start = time.time()
	dirs = {"webp": opj(swd, "webp")}
	with ThreadPoolExecutor(max_workers=threads) as executor:
		for _ in as_completed(
			[
				executor.submit(convertWithPIL, swd, dirs["webp"], inputFile)
				for inputFile in ls(dirs["webp"])
			]
		):
			converted += 1
	end = time.time()
	print(f"Time taken to convert {converted} stickers (static) - {end - start:.3f}s")
	print()
	return converted


def convertAnimated(swd: str, threads: int = 4, frameSkip: int = 1, scale: float = 1) -> int:
	"""Convert animated stickers to webp, gif and png

	Args:
		swd (str): the sticker working directory (downloads/packName)
		threads (int, optional): number of threads to pass to ThreadPoolExecutor. Defaults to 4.
		frameSkip (int, optional): skip n number of frames in the interest of
		optimisation with a quality trade-off. Defaults to 1.
		scale (float, optional): upscale/ downscale the images produced. Intended
		for optimisation with a quality trade-off. Defaults to 1.

	Returns:
		int: number of stickers successfully converted
	"""
	converted = 0
	start = time.time()
	dirs = {"tgs": opj(swd, "tgs"), "gif": opj(swd, "gif"), "webp_": opj(swd, "webp_animated")}
	doConvMultLottie = (
		lambda fm, fs, sc: len(
			asyncio.get_event_loop().run_until_complete(
				pyrlottie.convMultLottie(fm, frameSkip=fs, scale=sc)
			)
		)
		// 2
	)
	converted += doConvMultLottie(
		fm=[
			pyrlottie.FileMap(
				pyrlottie.LottieFile(stckr),
				{
					stckr.replace(dirs["tgs"], dirs["gif"]).replace("tgs", "gif"),
					stckr.replace(dirs["tgs"], dirs["webp_"]).replace("tgs", "webp"),
				},
			)
			for stckr in [i for i in ls(dirs["tgs"]) if i.endswith(".tgs")]
		],
		fs=frameSkip,
		sc=scale,
	)
	with ThreadPoolExecutor(max_workers=threads) as executor:
		for _ in as_completed(
			[
				executor.submit(convertWithPIL, swd, dirs["webp_"], inputFile, False)
				for inputFile in ls(dirs["webp_"])
			]
		):
			_.result()

	end = time.time()
	print(f"Time taken to convert {converted} stickers (animated) - {end - start:.3f}s")
	print()
	return converted
