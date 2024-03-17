"""
Conversion functionality for animated stickers.

implements the conversion functionality for the pyrlottie backend. exposing a
public function called `convertAnimated`, which is used to perform the conversion.

The `convertAnimated` function takes the following parameters:
    - swd (Path): The sticker working directory (downloads/packName).
    - _threads (int, optional): The number of threads to pass to ThreadPoolExecutor.
		Defaults to 4.
    - frameSkip (int, optional): Skip n number of frames in the interest of
		optimization with a quality trade-off. Defaults to 1.
    - scale (float, optional): Upscale/downscale the images produced. Intended
		for optimization with a quality trade-off. Defaults to 1.

"""

from __future__ import annotations

import asyncio
from pathlib import Path

import pyrlottie


def convertAnimated(swd: Path, _threads: int = 4, frameSkip: int = 1, scale: float = 1) -> int:
	"""Convert animated stickers to webp, gif and png.

	Args:
	----
		swd (Path): the sticker working directory (downloads/packName)
		threads (int, optional): number of threads to pass to ThreadPoolExecutor. Defaults to 4.
		frameSkip (int, optional): skip n number of frames in the interest of
		optimisation with a quality trade-off. Defaults to 1.
		scale (float, optional): upscale/ downscale the images produced. Intended
		for optimisation with a quality trade-off. Defaults to 1.

	Returns:
	-------
		int: number of stickers successfully converted

	"""
	converted = 0

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
