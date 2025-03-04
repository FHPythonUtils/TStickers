# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2025 - 2025/02/16

- be opinionated and install `rlottie-python` by default/ regardless
- set default backend to `rlottie-python` in the cli
- add `--fmt` to the cli, where the user can select a list of formats to convert to (default is png
  and webp formats)
- replace `--frameskip` with `--fps` as this is more intuitive

## 2024.1.3 - 2024/08/26

- clearly notify user if backend is not installed

## 2024.1.2 - 2024/03/25

- revert 'fix'

## 2024.1.1 - 2024/03/24

- fix `convert_rlottie_python.py`

## 2024.1 - 2024/03/22

- Add '--file' arg for passing in a list of packs
- Implement a custom `demojize` function similar to the `emoji.demojize` function.
	However, returns a string of unique keywords in alphabetical order seperated by "_"

## 2024 - 2024/03/17

- add convert backends to give the user a choice of using their preferred tool
- ruff
- code quality improvements

## 2022.1.1 - 2022/06/25

- Fix: add `parents=True` to `Path.mkdir()`
- Update pre-commit

## 2022.1 - 2022/02/01

- Refactor
- Add support for webm stickers

## 2022 - 2022/01/24

- Bump pillow version (CVE-2022-22815, CVE-2022-22816, CVE-2022-22817)
- Update deps
- Add formal tests

## 2021.4.4 - 2021/12/10

- Fix https://github.com/FHPythonUtils/SigStickers/issues/1
- More meaningful error messages

## 2021.4.2 - 2021/10/08

- Implement action='extend' for pre 3.7 eg. `python3 -m tstickers -p pack1 pack2 -p pack3`

## 2021.4.1 - 2021/10/04

- Update function names and docs

## 2021.4 - 2021/10/04

- Added caching functionality using requests_cache and to the converter -
	output cache hit/miss to stdout for converter

## 2021.3.3 - 2021/10/03

- Use `asyncio.get_event_loop().run_until_complete` in place of `asyncio.run` for compat
	with pyrlottie 2021.1
- Marginal performance improvements with pyrlottie 2021.1 (~3% so may be a fluke?)

	```txt
	Performance testing with https://t.me/addstickers/DonutTheDog on:
	OS: Windows 10 (2021/10/03)
	CPU: Intel(R) Core(TM) i7-10510U CPU @ 1.80GHz
	RAM: 16gb

	using pyrlottie (lottie2gif.exe + gif2webp.exe)
		~85s (frameskip=0, scale=1) (-5s)
		~47s (frameskip=1, scale=1) (0s)
		~33s (frameskip=2, scale=1) (-1s)
	```

## 2021.3.2 - 2021/10/03

- Produce pngs for animated stickers as in SigStickers
- Tidy up

## 2021.3.1 - 2021/10/02

- Bugfixes in dependency (pyrlottie) for linux/ wsl - so now runs

	```txt
	Performance testing with https://t.me/addstickers/DonutTheDog on:
	OS: Windows 10 WSL Ubuntu (2021/10/02)
	CPU: Intel(R) Core(TM) i7-10510U CPU @ 1.80GHz
	RAM: 16gb

	using pyrlottie (lottie2gif + gif2webp)
		~61s (frameskip=0, scale=1)
		~27s (frameskip=1, scale=1)
		~18s (frameskip=2, scale=1)

	=> Approximately a 3.5x speed improvement for like-to-like image quality
	=> Approximately a 2.4x speed improvement for improved image quality
	```

## 2021.3 - 2021/10/02

- code quality improvements (eg readability)
- significant performance improvements

	```txt
	Performance testing with https://t.me/addstickers/DonutTheDog on:
	OS: Windows 10 (2021/10/02)
	CPU: Intel(R) Core(TM) i7-10510U CPU @ 1.80GHz
	RAM: 16gb

	using pylottie (pyppeteer backend)
		~72s quality=1 (equal to frameskip=2)

	using pyrlottie (lottie2gif.exe + gif2webp.exe)
		~90s (frameskip=0, scale=1)
		~47s (frameskip=1, scale=1)
		~34s (frameskip=2, scale=1)
		~32s (frameskip=1, scale=0.5)

	=> Approximately a 2x speed improvement for like-to-like image quality
	=> Approximately a 1.4x speed improvement for improved image quality
	```

## 2021.2.1 - 2021/02/21

- Fix `ResourceWarning: unclosed ssl.SSLSocket`

## 2021.2 - 2021/01/19

- File names are now the emoji as text followed by the emoji glyph e.g.
	"647+smiling_face_with_3_hearts+🥰" followed by the file extension (requires
	`emoji` for this)
- If no animated stickers then puppeteer is not launched resulting in a small
	speed increase
- Strings double-quoted

## 2021.1.5 - 2021/01/13

- Update `pylottie` for significant speed improvements (animation renders take
	approx 2/3 as long)
- Leverage the quality setting exposed by `pylottie` to further improve speed if
	desired (quality 0 is fastest, quality 3 is best quality)

## 2021.1.3 - 2021/01/13

- Use `pylottie` to convert animated stickers increasing processing speed by about 10%
- Can pass in packs with `-p` or `--pack`
- Can also pass in the bot token with `-t` or `--token`

## 2021.1.2 - 2021/01/07

- Static stickers are saved as gif in addition to png and webp

## 2021.1.1 - 2021/01/07

- Save animated stickers as webp
- Fixed animation times

## 2021.1 - 2021/01/06

- Added animated sticker support
	- These are converted to gif
	- No transparency support at this time

## 2021.0.1 - 2021/01/04

- Using pillow for conversions

## 2021 - 2021/01/04

- First release
