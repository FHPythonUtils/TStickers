# Changelog
All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

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
