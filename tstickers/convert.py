"""Sticker convert functions used by the downloader."""
from __future__ import annotations

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import pyrlottie
from PIL import Image


def assureDirExists(root: Path, directory: Path | str) -> Path:
	"""make the dir if not exists

	Args:
		root (Path): the path of the root directory
		directory (Path|str): the directory name

	Returns:
		Path: the full path
	"""
	(root / directory).mkdir(parents=True, exist_ok=True)
	return root / directory


def convertWithPIL(inputFile: str) -> str:
	"""Convert the webp file to png

	Args:
		inputFile (str): path to input file

	Returns:
		str: path to input file
	"""
	img = Image.open(inputFile)
	img.save(inputFile.replace("webp", "png"))
	gifImage = inputFile.replace("webp", "gif")
	if not Path(gifImage).exists():
		img.save(gifImage)
	return inputFile


def convertWebp(swd: Path, threads: int = 4) -> int:
	"""Convert static stickers to png and gif

	Args:
		swd (Path): the sticker working directory (downloads/packName)
		threads (int, optional): number of threads to pass to ThreadPoolExecutor. Defaults to 4.

	Returns:
		int: number of stickers successfully converted
	"""
	converted = 0
	start = time.time()
	assureDirExists(swd, "png")
	assureDirExists(swd, "gif")
	with ThreadPoolExecutor(max_workers=threads) as executor:
		for _ in as_completed(
			[
				executor.submit(convertWithPIL, inputFile.as_posix())
				for inputFile in (swd / "webp").glob("**/*")
			]
		):
			converted += 1
	end = time.time()
	print(f"Time taken to convert {converted} stickers (webp) - {end - start:.3f}s")
	print()
	return converted


def convertTgs(swd: Path, threads: int = 4, frameSkip: int = 1, scale: float = 1) -> int:
	"""Convert animated stickers to webp, gif and png

	Args:
		swd (Path): the sticker working directory (downloads/packName)
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
	assureDirExists(swd, "gif")
	assureDirExists(swd, "webp")
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
				pyrlottie.LottieFile(stckr.absolute().as_posix()),
				{
					stckr.absolute().as_posix().replace("tgs", "gif"),
					stckr.absolute().as_posix().replace("tgs", "webp"),
				},
			)
			for stckr in swd.glob("**/*.tgs")
		],
		fs=frameSkip,
		sc=scale,
	)
	end = time.time()
	print(f"Time taken to convert {converted} stickers (tgs) - {end - start:.3f}s")
	print()
	return converted
