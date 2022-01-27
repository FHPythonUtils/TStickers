""" tests """
from __future__ import annotations

import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
PROJECT_DIR = Path(THISDIR).parent
sys.path.insert(0, str(PROJECT_DIR))

from tstickers.downloader import StickerDownloader

token = ""
for candidate in [PROJECT_DIR/"env.txt", PROJECT_DIR/"env"]:
	if candidate.exists():
		token = candidate.read_text(encoding="utf-8").strip()
if not token:
	raise RuntimeError(
		'!! Generate a bot token and paste in a file called "env". Send a '
		+ "message to @BotFather to get started"
	)


downloader = StickerDownloader(token)
downloader.cwd = f"{THISDIR}/data"

packs = [{"pack":"DonutTheDog","len":28}]


def test_getPack():
	stickerPack = downloader.getPack(packs[0]["pack"])
	assert stickerPack is not None
	assert len(stickerPack["files"]) == packs[0]["len"]


def test_downloadPack():
	stickerPack = downloader.getPack(packs[0]["pack"])
	assert stickerPack is not None
	downloader.downloadPack(stickerPack)
	assert len(list(Path(f"{downloader.cwd}/donutthedog/tgs").iterdir())) == packs[0]["len"]


def test_convertPack():
	stickerPack = downloader.getPack(packs[0]["pack"])
	assert stickerPack is not None
	downloader.downloadPack(stickerPack)
	downloader.convertPack(packs[0]["pack"], scale=0.05, noCache=True)
	assert len(list(Path(f"{downloader.cwd}/donutthedog/webp_animated").iterdir())) == packs[0]["len"]


