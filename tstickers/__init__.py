"""Download sticker packs from Telegram
"""
import argparse
import os
from pathlib import Path
from sys import exit as sysexit

from tstickers.downloader import StickerDownloader


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
		help="Pass in a pack url inline",
		action="append",
	)
	parser.add_argument(
		"--frameskip",
		help="Set frameskip. default=0",
		type=int,
		default=1,
	)
	parser.add_argument(
		"--scale",
		help="Set scale. default=1.0",
		type=float,
		default=1,
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
	names = args.pack
	if names is None:
		names = []
		while True:
			name = input("Enter sticker_set url (leave blank to stop): ").strip()
			if name == "":
				break
			names.append(name)
	names = [name.split("/")[-1] for name in names]
	downloader = StickerDownloader(token)
	for sset in names:
		print("=" * 60)
		stickerSet = downloader.getStickerSet(sset)
		if stickerSet is None:
			continue
		print("-" * 60)
		_ = downloader.downloadStickerSet(stickerSet)
		print("-" * 60)
		downloader.convertDir(sset, args.frameskip, args.scale)


if __name__ == "__main__":
	cli()
