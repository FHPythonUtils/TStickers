"""
Conversion functionality for animated stickers.

implements the conversion functionality for the pyrlottie backend. exposing a
public function called `convertAnimated`, which is used to perform the conversion.

"""

from __future__ import annotations

import asyncio
from pathlib import Path

import pyrlottie


def convertAnimated(
	swd: Path,
	_threads: int = 4,
	fps: int = 20,
	scale: float = 1,
	_formats: set[str] | None = None,
) -> int:
	"""Convert animated stickers, over a number of threads, at a given framerate, scale and to a
	set of formats.

	:param Path swd: The sticker working directory (e.g., downloads/packName).
	:param int _threads: This is ignored for the pyrlottie backend
	:param int fps: framerate of the converted sticker, affecting optimization and
	quality (default: 20)
	:param float scale: Scale factor for up/downscaling images, affecting optimization and
	quality (default: 1).
	:param set[str] | None _formats: This is ignored for the pyrlottie backend
	:return int: Number of stickers successfully converted.

	"""
	converted = 0

	(swd / "webp").mkdir(parents=True, exist_ok=True)
	(swd / "gif").mkdir(parents=True, exist_ok=True)

	# here we are going to assume that the raw image is 60 fps as pyrlottie does not have a way
	# of setting the fps
	frameSkip = 0
	if fps < 45:  # bisector of 30 and 60
		frameSkip = 1  # ~30fps
	if fps < 25:  # bisector of 20 and 30
		frameSkip = 2  # ~20fps
	if fps < 18:  # bisector of 15 and 20
		frameSkip = 3  # ~15fps
	if fps < 13:  # 12fps and below
		frameSkip = 4  # ~12fps

	def doConvMultLottie(filemaps: list[pyrlottie.FileMap], frameSkip: int, scale: float) -> int:
		return (
			len(
				asyncio.get_event_loop().run_until_complete(
					pyrlottie.convMultLottie(filemaps, frameSkip=frameSkip, scale=scale)
				)
			)
			// 2
		)

	converted += doConvMultLottie(
		filemaps=[
			pyrlottie.FileMap(
				pyrlottie.LottieFile(stckr.absolute().as_posix()),
				{
					stckr.absolute().as_posix().replace("tgs", "gif"),
					stckr.absolute().as_posix().replace("tgs", "webp"),
				},
			)
			for stckr in swd.glob("**/*.tgs")
		],
		frameSkip=frameSkip,
		scale=scale,
	)
	return converted
