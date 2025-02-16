"""Download sticker packs from Telegram."""

from __future__ import annotations

import argparse
import functools
import importlib.util
import operator
from pathlib import Path
from sys import exit as sysexit

from loguru import logger

from tstickers.convert import Backend
from tstickers.manager import StickerManager

allowed_formats = {"gif", "png", "webp", "apng"}


def cli() -> None:  # pragma: no cover
	"""Cli entry point."""
	parser = argparse.ArgumentParser("Welcome to TStickers, providing all of your sticker needs")
	parser.add_argument(
		"-t",
		"--token",
		help="Pass in a bot token inline",
	)
	parser.add_argument(
		"-p",
		"--pack",
		action="append",
		nargs="+",
		help="Pass in a pack url, or pack name",
	)
	parser.add_argument(
		"--fmt",
		action="append",
		nargs="+",
		choices=allowed_formats,
		help=f"Formats to convert to {allowed_formats}",
	)
	parser.add_argument(
		"-f",
		"--file",
		help="Path to file containing pack urls",
	)
	parser.add_argument(
		"--fps",
		default=20,
		type=int,
		help="Set fps. default=20",
	)
	parser.add_argument(
		"--scale",
		default=1,
		type=float,
		help="Set scale. default=1.0",
	)
	parser.add_argument(
		"-b",
		"--backend",
		choices={"rlottie_python", "pyrlottie"},
		default="pyrlottie",
		help="Specify the convert backend",
	)
	args = parser.parse_args()

	# Get the token
	token = args.token
	if token is None:
		token = ""
		for candidate in [Path.cwd() / "env.txt", Path.cwd() / "env"]:
			if candidate.exists():
				token = candidate.read_text(encoding="utf-8").strip()
		if not token:
			logger.error(
				'!! Generate a bot token and paste in a file called "env". Send a '
				"message to @BotFather to get started"
			)
			sysexit(1)
	# Get the backend
	backend = args.backend

	if importlib.util.find_spec(backend) is None:
		logger.error(f'!! {backend} is not installed! Install with "pip install {backend}"')
		sysexit(2)

	# Get the packs

	packs = []
	if args.file:
		fp = Path(args.file)
		if fp.is_file():
			packs = fp.read_text("utf-8").strip().splitlines()

	packs.extend(functools.reduce(operator.iadd, args.pack or [[]], []))
	if len(packs) == 0:
		logger.info("No packs provided, entering interactive mode...")
		while True:
			name = input("Enter pack url, or name (hit enter to stop):>").strip()
			if name == "":
				break
			packs.append(name)
	packs = [name.split("/")[-1] for name in packs]

	formats = {fmt for sublist in (args.fmt or []) for fmt in sublist}
	if len(formats) == 0:
		formats = allowed_formats

	downloader = StickerManager(token)
	for pack in packs:
		logger.info("-" * 60)
		_ = downloader.downloadPack(pack)
		logger.info("-" * 60)

		backend_map = {"rlottie_python": Backend.RLOTTIE_PYTHON, "pyrlottie": Backend.PYRLOTTIE}

		downloader.convertPack(
			pack,
			args.fps,
			args.scale,
			backend=backend_map.get(args.backend, Backend.PYRLOTTIE),
			formats=formats,
		)
