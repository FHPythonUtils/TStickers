"""tests"""

from __future__ import annotations

import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
PROJECT_DIR = Path(THISDIR).parent
sys.path.insert(0, str(PROJECT_DIR))

from tstickers.convert import Backend
from tstickers.manager import StickerManager

token = ""
for candidate in [PROJECT_DIR / "env.txt", PROJECT_DIR / "env"]:
	if candidate.exists():
		token = candidate.read_text(encoding="utf-8").strip()
if not token:
	msg = (
		'!! Generate a bot token and paste in a file called "env". Send a '
		"message to @BotFather to get started"
	)
	raise RuntimeError(msg)


stickerManager = StickerManager(token)
stickerManager.cwd = Path(THISDIR) / "data"

packs = [{"pack": "DonutTheDog", "len": 31}]


def test_getPack() -> None:
	stickerPack = stickerManager.getPack(packs[0]["pack"])
	assert stickerPack is not None
	assert len(stickerPack["files"]) == packs[0]["len"]


def test_downloadPack() -> None:
	stickerManager.downloadPack(packs[0]["pack"])
	assert len(list(Path(f"{stickerManager.cwd}/donutthedog/tgs").iterdir())) == packs[0]["len"]


def test_convertPack() -> None:
	stickerManager.downloadPack(packs[0]["pack"])
	stickerManager.convertPack(
		packs[0]["pack"], scale=0.05, noCache=True, backend=Backend.RLOTTIE_PYTHON
	)
	assert len(list(Path(f"{stickerManager.cwd}/donutthedog/webp").iterdir())) == packs[0]["len"]


# def test_convertPack_slow() -> None:
# 	stickerManager.downloadPack(packs[0]["pack"])
# 	stickerManager.convertPack(packs[0]["pack"], scale=1, noCache=True, backend=Backend.PYRLOTTIE)
# 	assert len(list(Path(f"{stickerManager.cwd}/donutthedog/webp").iterdir())) == packs[0]["len"]
