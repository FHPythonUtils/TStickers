
import asyncio
from pathlib import Path

import pyrlottie


def convertAnimated(swd: Path, threads: int = 4, frameSkip: int = 1, scale: float = 1) -> int:
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
	def doConvMultLottie(fm, fs, sc):
		return len(asyncio.get_event_loop().run_until_complete(pyrlottie.convMultLottie(fm, frameSkip=fs, scale=sc))) // 2
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
	return converted
