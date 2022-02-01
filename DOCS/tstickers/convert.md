# convert

> Auto-generated documentation for [tstickers.convert](../../tstickers/convert.py) module.

Sticker convert functions used by the downloader.

- [Tstickers](../README.md#tstickers-index) / [Modules](../README.md#tstickers-modules) / [tstickers](index.md#tstickers) / convert
    - [assureDirExists](#assuredirexists)
    - [convertTgs](#converttgs)
    - [convertWebp](#convertwebp)
    - [convertWithPIL](#convertwithpil)

## assureDirExists

[[find in source code]](../../tstickers/convert.py#L13)

```python
def assureDirExists(root: Path, directory: Path | str) -> Path:
```

make the dir if not exists

#### Arguments

- `root` *Path* - the path of the root directory
- `directory` *Path|str* - the directory name

#### Returns

- `Path` - the full path

## convertTgs

[[find in source code]](../../tstickers/convert.py#L72)

```python
def convertTgs(
    swd: Path,
    threads: int = 4,
    frameSkip: int = 1,
    scale: float = 1,
) -> int:
```

Convert animated stickers to webp, gif and png

#### Arguments

- `swd` *Path* - the sticker working directory (downloads/packName)
- `threads` *int, optional* - number of threads to pass to ThreadPoolExecutor. Defaults to 4.
- `frameSkip` *int, optional* - skip n number of frames in the interest of
optimisation with a quality trade-off. Defaults to 1.
- `scale` *float, optional* - upscale/ downscale the images produced. Intended
for optimisation with a quality trade-off. Defaults to 1.

#### Returns

- `int` - number of stickers successfully converted

## convertWebp

[[find in source code]](../../tstickers/convert.py#L44)

```python
def convertWebp(swd: Path, threads: int = 4) -> int:
```

Convert static stickers to png and gif

#### Arguments

- `swd` *Path* - the sticker working directory (downloads/packName)
- `threads` *int, optional* - number of threads to pass to ThreadPoolExecutor. Defaults to 4.

#### Returns

- `int` - number of stickers successfully converted

## convertWithPIL

[[find in source code]](../../tstickers/convert.py#L27)

```python
def convertWithPIL(inputFile: str) -> str:
```

Convert the webp file to png

#### Arguments

- `inputFile` *str* - path to input file

#### Returns

- `str` - path to input file
