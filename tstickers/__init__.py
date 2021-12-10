"""Download sticker packs from Telegram
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from sys import exit as sysexit

from .downloader import StickerDownloader


def cli():
	"""cli entry point"""
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
	args = parser.parse_args()
	# Get the token
	token = args.token
	if args.token is None:
		token = ""
		for candidate in [Path(os.getcwd() + "/env.txt"), Path(os.getcwd() + "/env")]:
			if candidate.exists():
				token = candidate.read_text(encoding="utf-8").strip()
		if not token:
			print(
				'!! Generate a bot token and paste in a file called "env". Send a '
				+ "message to @BotFather to get started"
			)
			sysexit(1)
	# Get the packs
	packs = sum(args.pack or [[]], [])
	if len(packs) == 0:
		packs = []
		while True:
			name = input("Enter sticker_set url (leave blank to stop): ").strip()
			if name == "":
				break
			packs.append(name)
	packs = [name.split("/")[-1] for name in packs]
	downloader = StickerDownloader(token)
	for pack in packs:
		print("=" * 60)
		stickerPack = downloader.getPack(pack)
		if stickerPack is None:
			continue
		print("-" * 60)
		_ = downloader.downloadPack(stickerPack)
		print("-" * 60)
		downloader.convertPack(pack, args.frameskip, args.scale)


if __name__ == "__main__":
	cli()
