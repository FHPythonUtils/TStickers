"""Download sticker packs from Telegram."""

from __future__ import annotations

import argparse
import functools
import operator
from pathlib import Path
from sys import exit as sysexit

from loguru import logger

from tstickers.convert import Backend
from tstickers.downloader import StickerDownloader


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
		help="Pass in a pack url inline",
	)
	parser.add_argument(
		"--frameskip",
		default=1,
		type=int,
		help="Set frameskip. default=1",
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
		choices=["rlottie-python", "pyrlottie"],
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
	# Get the packs
	packs = functools.reduce(operator.iadd, args.pack or [[]], [])
	if len(packs) == 0:
		while True:
			name = input("Enter sticker_set url (leave blank to stop): ").strip()
			if name == "":
				break
			packs.append(name)
	packs = [name.split("/")[-1] for name in packs]

	downloader = StickerDownloader(token)
	for pack in packs:
		logger.info("=" * 60)
		stickerPack = downloader.getPack(pack)
		if stickerPack is None:
			continue
		logger.info("-" * 60)
		_ = downloader.downloadPack(stickerPack)
		logger.info("-" * 60)

		backend_map = {"rlottie-python": Backend.RLOTTIE_PYTHON, "pyrlottie": Backend.PYRLOTTIE}

		downloader.convertPack(
			pack,
			args.frameskip,
			args.scale,
			backend=backend_map.get(args.backend, Backend.PYRLOTTIE),
		)
