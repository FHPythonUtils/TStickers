"""Sticker convert functions used by the downloader."""

from __future__ import annotations

import contextlib
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor
from enum import IntEnum, auto
from pathlib import Path

from loguru import logger
from PIL import Image


class Backend(IntEnum):
	"""Represents different conversion libraries such as pyrlottie, and rlottie-python."""

	UNDEFINED = -1
	PYRLOTTIE = auto()
	RLOTTIE_PYTHON = auto()


def convertAnimatedFunc(
	_swd: Path,
	_threads: int,
	_fps: int,
	_scale: float,
	_formats: set[str] | None,
) -> int:
	"""Convert animated stickers with (Base/Backend.UNDEFINED)."""
	msg = "Backend could not be loaded"
	raise RuntimeError(msg)


convertRlottiePython = convertPyRlottie = convertAnimatedFunc

with contextlib.suppress(ModuleNotFoundError):
	from tstickers.convert_rlottie_python import convertAnimated as convertRlottiePython
with contextlib.suppress(ModuleNotFoundError):
	from tstickers.convert_pyrlottie import convertAnimated as convertPyRlottie


def convertWithPIL(input_file: Path, formats: set[str]) -> Path:
	"""Convert a webp file to specified formats.

	:param Path input_file: path to the input image/ sticker
	:param set[str] formats: set of formats
	:return Path: path of the original image/sticker file
	"""

	img = Image.open(input_file)

	for fmt in formats:
		output_file = Path(input_file.as_posix().replace("webp", fmt))
		if not output_file.exists():
			img.save(output_file)

	return input_file


def convertStatic(
	swd: Path,
	threads: int = 4,
	formats: set[str] | None = None,
) -> int:
	"""Convert static stickers to specified formats.


	:param Path swd: The sticker working directory (e.g., downloads/packName).
	:param int threads: Number of threads for ProcessPoolExecutor (default: number of
	logical processors).
	:param set[str]|None formats: Set of formats to convert telegram webp stickers to
	(default: {"gif", "png", "webp", "apng"})
	:return int: Number of stickers successfully converted.

	"""
	if formats is None:
		formats = {"gif", "png", "webp", "apng"}
	webp_files = list((swd / "webp").glob("**/*.webp"))
	converted = 0
	start = time.time()

	with ThreadPoolExecutor(max_workers=threads) as executor:
		results = executor.map(lambda f: convertWithPIL(f, formats), webp_files)
		converted = sum(1 for _ in results)

	end = time.time()
	logger.info(f"Converted {converted} stickers (static) in {end - start:.3f}s\n")
	return converted


def convertAnimated(
	swd: Path,
	threads: int = multiprocessing.cpu_count(),
	fps: int = 20,
	scale: float = 1,
	backend: Backend = Backend.UNDEFINED,
	formats: set[str] | None = None,
) -> int:
	"""Convert animated stickers, over a number of threads, at a given framerate, scale and to a
	set of formats.

	:param Path swd: The sticker working directory (e.g., downloads/packName).
	:param int threads: Number of threads for ProcessPoolExecutor (default: number of
	logical processors).
	:param int fps: framerate of the converted sticker, affecting optimization and
	quality (default: 20)
	:param float scale: Scale factor for up/downscaling images, affecting optimization and
	quality (default: 1).
	:param set[str]|None formats: Set of formats to convert telegram tgs stickers to
	(default: {"gif", "webp", "apng"})
	:return int: Number of stickers successfully converted.

	"""
	if formats is None:
		formats = {"gif", "webp", "apng"}
	if backend == Backend.UNDEFINED:
		msg = "You must specify a conversion backend"
		raise RuntimeError(msg)
	start = time.time()

	convertMap = {
		Backend.UNDEFINED: convertAnimatedFunc,
		Backend.PYRLOTTIE: convertPyRlottie,
		Backend.RLOTTIE_PYTHON: convertRlottiePython,
	}

	converted = convertMap[backend](swd, threads, fps, scale, formats)

	end = time.time()
	logger.info(f"Time taken to convert {converted} stickers (tgs) - {end - start:.3f}s")
	logger.info("")
	return converted
