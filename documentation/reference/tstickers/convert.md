# Convert

[Tstickers Index](../README.md#tstickers-index) /
[Tstickers](./index.md#tstickers) /
Convert

> Auto-generated documentation for [tstickers.convert](../../../tstickers/convert.py) module.

- [Convert](#convert)
  - [assureDirExists](#assuredirexists)
  - [convertTgs](#converttgs)
  - [convertWebp](#convertwebp)
  - [convertWithPIL](#convertwithpil)

## assureDirExists

[Show source in convert.py:13](../../../tstickers/convert.py#L13)

make the dir if not exists

#### Arguments

- `root` *Path* - the path of the root directory
- `directory` *Path|str* - the directory name

#### Returns

- `Path` - the full path

#### Signature

```python
def assureDirExists(root: Path, directory: Path | str) -> Path:
    ...
```



## convertTgs

[Show source in convert.py:72](../../../tstickers/convert.py#L72)

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

#### Signature

```python
def convertTgs(swd: Path, threads: int = 4, frameSkip: int = 1, scale: float = 1) -> int:
    ...
```



## convertWebp

[Show source in convert.py:44](../../../tstickers/convert.py#L44)

Convert static stickers to png and gif

#### Arguments

- `swd` *Path* - the sticker working directory (downloads/packName)
- `threads` *int, optional* - number of threads to pass to ThreadPoolExecutor. Defaults to 4.

#### Returns

- `int` - number of stickers successfully converted

#### Signature

```python
def convertWebp(swd: Path, threads: int = 4) -> int:
    ...
```



## convertWithPIL

[Show source in convert.py:27](../../../tstickers/convert.py#L27)

Convert the webp file to png

#### Arguments

- `inputFile` *str* - path to input file

#### Returns

- `str` - path to input file

#### Signature

```python
def convertWithPIL(inputFile: str) -> str:
    ...
```


