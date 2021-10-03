# Changelog
All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

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

	using pyrlottie (lottie2gif.exe + gif2webp.exe)
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
