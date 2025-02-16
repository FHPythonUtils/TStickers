"""
Conversion functionality for animated stickers.

implements the conversion functionality for the rlottie_python backend. exposing a
public function called `convertAnimated`, which is used to perform the conversion.
"""

from __future__ import annotations

import concurrent.futures
import multiprocessing
from pathlib import Path

from loguru import logger
from rlottie_python import LottieAnimation


def convert_single_tgs(
	stckr: Path,
	fps: int,
	scale: float = 1.0,
	formats: set[str] | None = None,
) -> int:
	"""Convert a single tgs file.

	:param Path stckr: Path to the sticker
	:param int fps: framerate of the converted sticker, affecting optimization and
	quality (default: 20)
	:param float scale: Scale factor for up/downscaling images, affecting optimization and
	quality (default: 1).
	:param set[str]|None formats: Set of formats to convert telegram tgs stickers to
	(default: {"gif", "webp", "apng"})
	:return int: 1 if success

	"""
	tgs_file = stckr.absolute().as_posix()
	if formats is None:
		formats = {"gif", "webp", "apng"}

	# Read the animation outside the context manager to avoid issues with pickling
	anim = LottieAnimation.from_tgs(path=tgs_file)

	try:
		width, height = anim.lottie_animation_get_size()
		fps_orig = anim.lottie_animation_get_framerate()
		fps = min(fps, fps_orig)
		width = int(width * scale)
		height = int(height * scale)

		for format in formats:
			anim.save_animation(tgs_file.replace("tgs", format), fps, width=width, height=height)

	finally:
		anim.lottie_animation_destroy()

	return 1


def convertAnimated(
	swd: Path,
	threads: int = multiprocessing.cpu_count(),
	fps: int = 20,
	scale: float = 1,
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
	converted = 0

	with concurrent.futures.ProcessPoolExecutor(max_workers=threads) as executor:
		# Using list comprehension to submit tasks to the executor
		future_to_variable = {
			executor.submit(convert_single_tgs, stckr, fps, scale, formats): stckr
			for stckr in swd.glob("**/*.tgs")
		}

		# Wait for all tasks to complete and retrieve results
		for future in concurrent.futures.as_completed(future_to_variable):
			variable = future_to_variable[future]
			try:
				converted += future.result()
			except Exception as e:
				logger.error(f"Error processing {variable}: {e}")

	return converted
