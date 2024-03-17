# Convert

[Tstickers Index](../README.md#tstickers-index) / [Tstickers](./index.md#tstickers) / Convert

> Auto-generated documentation for [tstickers.convert](../../../tstickers/convert.py) module.

- [Convert](#convert)
  - [Backend](#backend)
  - [assureDirExists](#assuredirexists)
  - [convertAnimated](#convertanimated)
  - [convertFunc](#convertfunc)
  - [convertStatic](#convertstatic)
  - [convertWithPIL](#convertwithpil)

## Backend

[Show source in convert.py:15](../../../tstickers/convert.py#L15)

#### Signature

```python
class Backend(IntEnum): ...
```



## assureDirExists

[Show source in convert.py:33](../../../tstickers/convert.py#L33)

Make the dir if not exists.

#### Arguments

----
 - `root` *Path* - the path of the root directory
 - `directory` *Path|str* - the directory name

#### Returns

-------
 - `Path` - the full path

#### Signature

```python
def assureDirExists(root: Path, directory: Path | str) -> Path: ...
```



## convertAnimated

[Show source in convert.py:101](../../../tstickers/convert.py#L101)

Convert animated stickers to webp, gif and png.

#### Arguments

----
 - `swd` *Path* - the sticker working directory (downloads/packName)
 - `threads` *int, optional* - number of threads to pass to ThreadPoolExecutor. Defaults to number of cores/ logical processors.
 - `frameSkip` *int, optional* - skip n number of frames in the interest of
 optimisation with a quality trade-off. Defaults to 1.
 - `scale` *float, optional* - upscale/ downscale the images produced. Intended
 for optimisation with a quality trade-off. Defaults to 1.

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



## convertFunc

[Show source in convert.py:21](../../../tstickers/convert.py#L21)

#### Signature

```python
def convertFunc(_x, _y, _z, _a) -> int: ...
```



## convertStatic

[Show source in convert.py:70](../../../tstickers/convert.py#L70)

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

[Show source in convert.py:50](../../../tstickers/convert.py#L50)

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