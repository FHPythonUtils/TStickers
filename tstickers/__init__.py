"""Entry point for python -m sigstickers."""

import sys

from loguru import logger

from tstickers.cli import cli

_ = cli


logger.remove(0)
logger.add(
	sys.stderr,
	format="<level>{level: <8}</level> | <level>{message}</level>",
)
