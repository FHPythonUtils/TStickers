"""Sticker caching functionality used by the downloader."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from requests_cache.session import CachedSession

# requests_cache
cachedSession = CachedSession(
	".cache/tstickers.requests.sqlite",
	backend="sqlite",
	expire_after=60 * 60 * 12,
	allowable_codes=(200,),
	allowable_methods=("GET", "POST"),
)


def verifyConverted(packName: str) -> bool:
	"""Verify the cache for a packName eg. "DonutTheDog". Uses the cache "version"
	to call the verify function for that version

	Args:
		packName (str): name of the sticker pack eg. "DonutTheDog"

	Returns:
		bool: if the converted cache has been verified
	"""
	cache = Path(f".cache/{packName}")
	if cache.exists():
		data = json.loads(cache.read_text(encoding="utf-8"))
		try:
			if [None, _verifyConvertedV1][data["version"]](data):
				print(f"-> Cache hit for {packName}!")
				return True
		except KeyError:
			pass
	print(f"-> Cache miss for {packName}!")
	return False


def _verifyConvertedV1(data: dict[str, Any]):
	"""Verify the cache for a packName using cache data

	Args:
		data (dict[str, Any]) packName cache data to verify

	Returns:
		bool: if the converted cache has been verified
	"""
	return (
		Path(f"{data['info']['swd']}/webp_animated").exists()
		and data["converted"]["static"] + data["converted"]["animated"]
		== data["converted"]["total"]
	)


def createConverted(packName: str, data: dict):
	"""Write cache data to a file identified by packName

	Args:
		packName (str): name of the sticker pack eg. "DonutTheDog"
		data (dict): packName cache data to write to cache
	"""
	cache = Path(f".cache/{packName}")
	cache.write_text(json.dumps(data), encoding="utf-8")
