"""
Conversion functionality for animated stickers.

implements the conversion functionality for the rlottie_python backend. exposing a
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

import concurrent.futures
import multiprocessing
from pathlib import Path

from loguru import logger
from rlottie_python import LottieAnimation


def convert_single_tgs(stckr: Path, fps: int, scale: float = 1.0) -> int:
	tgs_file = stckr.absolute().as_posix()

	# Read the animation outside the context manager to avoid issues with pickling
	anim = LottieAnimation.from_tgs(path=tgs_file)

	try:
		width, height = anim.lottie_animation_get_size()
		fps_orig = anim.lottie_animation_get_framerate()
		fps = min(fps, fps_orig)
		width = int(width * scale)
		height = int(height * scale)

		anim.save_animation(tgs_file.replace("tgs", "apng"), fps, width=width, height=height)
		anim.save_animation(tgs_file.replace("tgs", "gif"), fps, width=width, height=height)
		anim.save_animation(tgs_file.replace("tgs", "webp"), fps, width=width, height=height)

	finally:
		anim.lottie_animation_destroy()

	return 1


def convertAnimated(
	swd: Path,
	threads: int = multiprocessing.cpu_count(),
	frameSkip: int = 1,
	scale: float = 1,
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

	Returns:
	-------
		int: number of stickers successfully converted

	"""
	converted = 0

	fps = [None, 30, 20, 15, 12][min(4, max(0, frameSkip))]

	with concurrent.futures.ProcessPoolExecutor(max_workers=threads) as executor:
		# Using list comprehension to submit tasks to the executor
		future_to_variable = {
			executor.submit(convert_single_tgs, stckr, fps, scale): stckr
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
