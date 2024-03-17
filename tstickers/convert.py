"""Sticker convert functions used by the downloader."""

from __future__ import annotations

import contextlib
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from enum import IntEnum, auto
from pathlib import Path

from PIL import Image


class Backend(IntEnum):
	UNDEFINED = -1
	PYRLOTTIE = auto()
	RLOTTIE_PYTHON = auto()


def convertFunc(_x, _y, _z, _a) -> int:
	raise RuntimeError("Backend could not be loaded")


convertRlottiePython = convertPyRlottie = convertFunc

with contextlib.suppress(ModuleNotFoundError):
	from tstickers.convert_rlottie_python import convertAnimated as convertRlottiePython
with contextlib.suppress(ModuleNotFoundError):
	from tstickers.convert_pyrlottie import convertAnimated as convertPyRlottie


def assureDirExists(root: Path, directory: Path | str) -> Path:
	"""Make the dir if not exists.

	Args:
	----
		root (Path): the path of the root directory
		directory (Path|str): the directory name

	Returns:
	-------
		Path: the full path

	"""
	(root / directory).mkdir(parents=True, exist_ok=True)
	return root / directory


def convertWithPIL(inputFile: str) -> str:
	"""Convert the webp file to png.

	Args:
	----
		inputFile (str): path to input file

	Returns:
	-------
		str: path to input file

	"""
	img = Image.open(inputFile)
	img.save(inputFile.replace("webp", "png"))
	gifImage = inputFile.replace("webp", "gif")
	if not Path(gifImage).exists():
		img.save(gifImage)
	return inputFile


def convertStatic(swd: Path, threads: int = 4) -> int:
	"""Convert static stickers to png and gif.

	Args:
	----
		swd (Path): the sticker working directory (downloads/packName)
		threads (int, optional): number of threads to pass to ThreadPoolExecutor. Defaults to 4.

	Returns:
	-------
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


def convertAnimated(
	swd: Path,
	threads: int = multiprocessing.cpu_count(),
	frameSkip: int = 1,
	scale: float = 1,
	backend: Backend = Backend.UNDEFINED,
) -> int:
	"""Convert animated stickers to webp, gif and png.

	Args:
	----
		swd (Path): the sticker working directory (downloads/packName)
		threads (int, optional): number of threads to pass to ThreadPoolExecutor. Defaults to number of cores/ logical processors.
		frameSkip (int, optional): skip n number of frames in the interest of
		optimisation with a quality trade-off. Defaults to 1.
		scale (float, optional): upscale/ downscale the images produced. Intended
		for optimisation with a quality trade-off. Defaults to 1.

	Returns:
	-------
		int: number of stickers successfully converted

	"""
	if backend == Backend.UNDEFINED:
		raise RuntimeError("You must specify a conversion backend")
	start = time.time()
	assureDirExists(swd, "apng")
	assureDirExists(swd, "gif")
	assureDirExists(swd, "webp")

	convertMap = {
		Backend.UNDEFINED: convertFunc,
		Backend.PYRLOTTIE: convertPyRlottie,
		Backend.RLOTTIE_PYTHON: convertRlottiePython,
	}

	converted = convertMap[backend](swd, threads, frameSkip, scale)

	end = time.time()
	print(f"Time taken to convert {converted} stickers (tgs) - {end - start:.3f}s")
	print()
	return converted
