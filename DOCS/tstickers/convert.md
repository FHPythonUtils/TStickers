# convert

> Auto-generated documentation for [tstickers.convert](../../tstickers/convert.py) module.

Sticker convert functions used by the downloader.

- [Tstickers](../README.md#tstickers-index) / [Modules](../README.md#tstickers-modules) / [tstickers](index.md#tstickers) / convert
    - [convertAnimated](#convertanimated)
    - [convertStatic](#convertstatic)
    - [convertWithPIL](#convertwithpil)
    - [ls](#ls)

## convertAnimated

[[find in source code]](../../tstickers/convert.py#L78)

```python
def convertAnimated(
    swd: str,
    threads: int = 4,
    frameSkip: int = 1,
    scale: float = 1,
) -> int:
```

Convert animated stickers to webp, gif and png

#### Arguments

- `swd` *str* - the sticker working directory (downloads/packName)
- `threads` *int, optional* - number of threads to pass to ThreadPoolExecutor. Defaults to 4.
- `frameSkip` *int, optional* - skip n number of frames in the interest of
optimisation with a quality trade-off. Defaults to 1.
- `scale` *float, optional* - upscale/ downscale the images produced. Intended
for optimisation with a quality trade-off. Defaults to 1.

#### Returns

- `int` - number of stickers successfully converted

## convertStatic

[[find in source code]](../../tstickers/convert.py#L51)

```python
def convertStatic(swd: str, threads: int = 4) -> int:
```

Convert static stickers to png and gif

#### Arguments

- `swd` *str* - the sticker working directory (downloads/packName)
- `threads` *int, optional* - number of threads to pass to ThreadPoolExecutor. Defaults to 4.

#### Returns

- `int` - number of stickers successfully converted

## convertWithPIL

[[find in source code]](../../tstickers/convert.py#L28)

```python
def convertWithPIL(
    swd: str,
    srcDir: str,
    inputFile: str,
    static: bool = True,
) -> str:
```

Convert the webp file to png

#### Arguments

- `swd` *str* - sticker working directory
- `srcDir` *str* - sticker src directory
- `inputFile` *str* - path to input file
- `static` *bool* - for static stickers

#### Returns

- `str` - path to input file

## ls

[[find in source code]](../../tstickers/convert.py#L16)

```python
def ls(directory: str) -> list[str]:
```

Do an ls

#### Arguments

- `directory` *str* - directory to ls

#### Returns

- `list[str]` - list of file paths
