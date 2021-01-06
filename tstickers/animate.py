from __future__ import annotations
from typing import Tuple
"""Support for animated stickers
"""

import gzip
import json
import asyncio
from pyppeteer import launch
from PIL import Image

from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)


def convertTGS2GIF(fileName: str, newFileName: str):
	"""Convert a tgs to gif

	Args:
		fileName (str): file path of the tgs
		newFileName (str): file path of the gif
	"""
	archive = gzip.open(fileName, "rb")
	lottie = json.load(archive)
	duration, numFrames = asyncio.get_event_loop(
	).run_until_complete(recordLottie(json.dumps(lottie)))
	images = []
	for frame in range(0, numFrames, 2):
		images.append(Image.open("temp/temp{}.png".format(frame)))
	images[0].save(newFileName, save_all=True, append_images=images[1:],
	duration=duration / 2, loop=0, transparency=0, disposal=2)


async def recordLottie(lottieData: str) -> Tuple[int, int]:
	"""Record the lottie data to a set of images

	Args:
		lottieData (str): lottie data as string

	Returns:
		Tuple[int, int]: duration and number of frames
	"""
	lottie = json.loads(lottieData)
	html = open(THISDIR + "/animate.html").read().replace("lottieData",
	lottieData).replace("THISDIR", THISDIR.replace("\\",
	"/")).replace("WIDTH", str(lottie["w"])).replace("HEIGHT", str(lottie["h"]))
	browser = await launch(headless=True,
	options={'args': ['--no-sandbox', "--disable-web-security",
	"--allow-file-access-from-files"]}) # yapf: disable
	page = await browser.newPage()
	await page.setContent(html)
	await page.waitForSelector('.ready')
	duration = await page.evaluate("() => duration")
	numFrames = await page.evaluate("() => numFrames")
	pageFrame = page.mainFrame
	rootHandle = await pageFrame.querySelector('#root')
	# Take a screenshot of each frame
	for count in range(0, numFrames, 2):
		await rootHandle.screenshot({
		'path': 'temp/temp{}.png'.format(count), "omitBackground": True, })
		await page.evaluate("animation.goToAndStop({}, true)".format(count + 1))
	return duration, numFrames
