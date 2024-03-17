"""Sticker caching functionality used by the downloader."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

from loguru import logger
from requests_cache.session import CachedSession

# requests_cache
cachedSession = CachedSession(
	".cache/tstickers.requests.sqlite",
	backend="sqlite",
	expire_after=60 * 60 * 12,
	allowable_codes=(200,),
	allowable_methods=("GET", "POST"),
)


CACHE_DIR = Path(".cache")
if not CACHE_DIR.exists():
	CACHE_DIR.mkdir()


def verify_converted(pack_name: str) -> bool:
	"""Verify the cache for a packName eg. "DonutTheDog". Uses the cache "version"
	to call the verify function for that version.

	Args:
	----
		pack_name (str): name of the sticker pack eg. "DonutTheDog"

	Returns:
	-------
		bool: if the converted cache has been verified

	"""
	cache = CACHE_DIR / pack_name
	if cache.exists():
		data = json.loads(cache.read_text(encoding="utf-8"))
		verify_func = _get_verify_function(data.get("version", 1))
		if verify_func(data):
			logger.info(f"-> Cache hit for {pack_name}!")
			return True
	logger.info(f"-> Cache miss for {pack_name}!")
	return False


def _verify_converted_v1(data: dict[str, Any]) -> bool:
	"""Verify the cache for a packName using cache data.

	Args:
	----
		data (dict[Path, Any]): packName cache data to verify

	Returns:
	-------
		bool: if the converted cache has been verified

	"""
	return (
		len(list(Path(f"{data['info']['swd']}").glob("**/*"))) > 0
		and data["converted"]["static"] + data["converted"]["animated"]
		>= data["converted"]["total"]
	)


def create_converted(pack_name: str, data: dict) -> None:
	"""Write cache data to a file identified by packName.

	Args:
	----
		pack_name (str): name of the sticker pack eg. "DonutTheDog"
		data (dict): packName cache data to write to cache

	"""
	cache = CACHE_DIR / pack_name
	cache.write_text(json.dumps(data), encoding="utf-8")


def _get_verify_function(version: int) -> Callable[[dict[str, Any]], bool]:
	"""Get the appropriate cache verification function based on version.

	Args:
	----
		version (int): Cache version

	Returns:
	-------
		Callable[[dict[str, Any]], bool]: Cache verification function

	"""
	return {
		1: _verify_converted_v1,
	}.get(version, _verify_converted_v1)
