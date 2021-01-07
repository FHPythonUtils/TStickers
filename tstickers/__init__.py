"""Download sticker packs from Telegram
"""
import os
from sys import exit as sysexit
from tstickers.downloader import StickerDownloader


def cli():
	""" cli entry point """
	try:
		token = open(os.getcwd() + "/env", encoding="utf-8").readline().strip()
	except FileNotFoundError:
		try:
			token = open(os.getcwd() + "/env.txt", encoding="utf-8").readline().strip()
		except FileNotFoundError:
			print("!! Generate a bot token and paste in a file called 'env'. Send a "+
			"message to @BotFather to get started")
			sysexit(1)
	downloader = StickerDownloader(token)
	print('Welcome to TSticker, providing all of your sticker needs')
	names = []
	while True:
		name = input("Enter sticker_set url (leave blank to stop): ").strip()
		if name == '':
			break

		names.append(name.split('/')[-1])

	for sset in names:
		print('=' * 60)
		stickerSet = downloader.getStickerSet(sset)
		if stickerSet is None:
			continue
		print('-' * 60)
		_ = downloader.downloadStickerSet(stickerSet)
		print('-' * 60)
		downloader.convertDir(sset)


if __name__ == "__main__":
	cli()
