# Convert

[Tstickers Index](../README.md#tstickers-index) / [Tstickers](./index.md#tstickers) / Convert

> Auto-generated documentation for [tstickers.convert](../../../tstickers/convert.py) module.

- [Convert](#convert)
  - [Backend](#backend)
  - [assure_dir_exists](#assure_dir_exists)
  - [convertAnimated](#convertanimated)
  - [convertAnimatedFunc](#convertanimatedfunc)
  - [convertStatic](#convertstatic)
  - [convertWithPIL](#convertwithpil)

## Backend

[Show source in convert.py:16](../../../tstickers/convert.py#L16)

Represents different conversion libraries such as pyrlottie, and rlottie-python.

#### Signature

```python
class Backend(IntEnum): ...
```



## assure_dir_exists

[Show source in convert.py:38](../../../tstickers/convert.py#L38)

Make the directory if it does not exist.

#### Arguments

----
 - `parts` *Path* - path parts

#### Returns

-------
 - `Path` - the full path

#### Signature

```python
def assure_dir_exists(*parts: Path | str) -> Path: ...
```



## convertAnimated

[Show source in convert.py:106](../../../tstickers/convert.py#L106)

Convert animated stickers to webp, gif and png.

#### Arguments

----
 - `swd` *Path* - the sticker working directory (downloads/packName)
 - `threads` *int, optional* - number of threads to pass to ThreadPoolExecutor. Defaults
  to number of cores/ logical processors.
 - `frameSkip` *int, optional* - skip n number of frames in the interest of
 optimisation with a quality trade-off. Defaults to 1.
 - `scale` *float, optional* - upscale/ downscale the images produced. Intended
 for optimisation with a quality trade-off. Defaults to 1.
 - `backend` *Backend* - The backend to use for conversion. Defaults to Backend.UNDEFINED,
allowing the system to determine the appropriate library to use.

#### Returns

-------
 - `int` - number of stickers successfully converted

#### Signature

```python
def convertAnimated(
    swd: Path,
    threads: int = multiprocessing.cpu_count(),
    frameSkip: int = 1,
    scale: float = 1,
    backend: Backend = Backend.UNDEFINED,
) -> int: ...
```

#### See also

- [Backend](#backend)



## convertAnimatedFunc

[Show source in convert.py:24](../../../tstickers/convert.py#L24)

Convert animated stickers with (Base/Backend.UNDEFINED).

#### Signature

```python
def convertAnimatedFunc(
    _swd: Path, _threads: int, _frameSkip: int, _scale: float
) -> int: ...
```



## convertStatic

[Show source in convert.py:75](../../../tstickers/convert.py#L75)

Convert static stickers to png and gif.

#### Arguments

----
 - `swd` *Path* - the sticker working directory (downloads/packName)
 - `threads` *int, optional* - number of threads to pass to ThreadPoolExecutor. Defaults to 4.

#### Returns

-------
 - `int` - number of stickers successfully converted

#### Signature

```python
def convertStatic(swd: Path, threads: int = 4) -> int: ...
```



## convertWithPIL

[Show source in convert.py:55](../../../tstickers/convert.py#L55)

Convert the webp file to png.

#### Arguments

----
 - `inputFile` *str* - path to input file

#### Returns

-------
 - `str` - path to input file

#### Signature

```python
def convertWithPIL(inputFile: str) -> str: ...
```