"""Download sticker packs from Telegram
"""
import os
import argparse
from sys import exit as sysexit
from tstickers.downloader import StickerDownloader


def cli():
	""" cli entry point """
	parser = argparse.ArgumentParser("Welcome to TSticker, providing all of your sticker needs")
	parser.add_argument("-t", "--token", help="Pass in a bot token inline")
	parser.add_argument("-p", "--pack", help="Pass in a pack url inline", action="append")
	parser.add_argument("-q", "--quality", help="Set animation quality. default=1", type=int, default=1)
	args = parser.parse_args()
	# Get the token
	token = args.token
	if args.token is None:
		try:
			token = open(os.getcwd() + "/env", encoding="utf-8").readline().strip()
		except FileNotFoundError:
			try:
				token = open(os.getcwd() + "/env.txt", encoding="utf-8").readline().strip()
			except FileNotFoundError:
				print("!! Generate a bot token and paste in a file called 'env'. Send a "+
				"message to @BotFather to get started")
				sysexit(1)
	# Get the packs
	names = args.pack
	if names is None:
		names = []
		while True:
			name = input("Enter sticker_set url (leave blank to stop): ").strip()
			if name == '':
				break
			names.append(name)
	names = [name.split("/")[-1] for name in names]
	downloader = StickerDownloader(token)
	for sset in names:
		print('=' * 60)
		stickerSet = downloader.getStickerSet(sset)
		if stickerSet is None:
			continue
		print('-' * 60)
		_ = downloader.downloadStickerSet(stickerSet)
		print('-' * 60)
		downloader.convertDir(sset, args.quality)

if __name__ == "__main__":
	cli()
