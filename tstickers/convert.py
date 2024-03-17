"""Sticker convert functions used by the downloader."""

from __future__ import annotations

import contextlib
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from enum import IntEnum, auto
from pathlib import Path

from loguru import logger
from PIL import Image


class Backend(IntEnum):
	"""Represents different conversion libraries such as pyrlottie, and rlottie-python."""

	UNDEFINED = -1
	PYRLOTTIE = auto()
	RLOTTIE_PYTHON = auto()


def convertAnimatedFunc(_swd: Path, _threads: int, _frameSkip: int, _scale: float) -> int:
	"""Convert animated stickers with (Base/Backend.UNDEFINED)."""
	msg = "Backend could not be loaded"
	raise RuntimeError(msg)


convertRlottiePython = convertPyRlottie = convertAnimatedFunc

with contextlib.suppress(ModuleNotFoundError):
	from tstickers.convert_rlottie_python import convertAnimated as convertRlottiePython
with contextlib.suppress(ModuleNotFoundError):
	from tstickers.convert_pyrlottie import convertAnimated as convertPyRlottie


def assure_dir_exists(*parts: Path | str) -> Path:
	"""Make the directory if it does not exist.

	Args:
	----
		parts (Path): path parts

	Returns:
	-------
		Path: the full path

	"""
	full_path = Path(*parts)
	full_path.mkdir(parents=True, exist_ok=True)
	return full_path


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
	assure_dir_exists(swd, "png")
	assure_dir_exists(swd, "gif")
	with ThreadPoolExecutor(max_workers=threads) as executor:
		for _ in as_completed(
			[
				executor.submit(convertWithPIL, inputFile.as_posix())
				for inputFile in (swd / "webp").glob("**/*")
			]
		):
			converted += 1
	end = time.time()
	logger.info(f"Time taken to convert {converted} stickers (webp) - {end - start:.3f}s")
	logger.info("")
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
		threads (int, optional): number of threads to pass to ThreadPoolExecutor. Defaults
			to number of cores/ logical processors.
		frameSkip (int, optional): skip n number of frames in the interest of
		optimisation with a quality trade-off. Defaults to 1.
		scale (float, optional): upscale/ downscale the images produced. Intended
		for optimisation with a quality trade-off. Defaults to 1.
		backend (Backend): The backend to use for conversion. Defaults to Backend.UNDEFINED,
	allowing the system to determine the appropriate library to use.

	Returns:
	-------
		int: number of stickers successfully converted

	"""
	if backend == Backend.UNDEFINED:
		msg = "You must specify a conversion backend"
		raise RuntimeError(msg)
	start = time.time()
	assure_dir_exists(swd, "apng")
	assure_dir_exists(swd, "gif")
	assure_dir_exists(swd, "webp")

	convertMap = {
		Backend.UNDEFINED: convertAnimatedFunc,
		Backend.PYRLOTTIE: convertPyRlottie,
		Backend.RLOTTIE_PYTHON: convertRlottiePython,
	}

	converted = convertMap[backend](swd, threads, frameSkip, scale)

	end = time.time()
	logger.info(f"Time taken to convert {converted} stickers (tgs) - {end - start:.3f}s")
	logger.info("")
	return converted
