# Convert

[Tstickers Index](../README.md#tstickers-index) / [Tstickers](./index.md#tstickers) / Convert

> Auto-generated documentation for [tstickers.convert](../../../tstickers/convert.py) module.

- [Convert](#convert)
  - [Backend](#backend)
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



## convertAnimated

[Show source in convert.py:93](../../../tstickers/convert.py#L93)

Convert animated stickers, over a number of threads, at a given framerate, scale and to a
set of formats.

#### Arguments

- `swd` *Path* - The sticker working directory (e.g., downloads/packName).
- `threads` *int* - Number of threads for ProcessPoolExecutor (default: number of
logical processors).
- `fps` *int* - framerate of the converted sticker, affecting optimization and
quality (default: 20)
- `scale` *float* - Scale factor for up/downscaling images, affecting optimization and
quality (default: 1).
:param set[str]|None formats: Set of formats to convert telegram tgs stickers to
(default: {"gif", "webp", "apng"})

#### Returns

Type: *int*
Number of stickers successfully converted.

#### Signature

```python
def convertAnimated(
    swd: Path,
    threads: int = multiprocessing.cpu_count(),
    fps: int = 20,
    scale: float = 1,
    backend: Backend = Backend.UNDEFINED,
    formats: set[str] | None = None,
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
    _swd: Path, _threads: int, _fps: int, _scale: float, _formats: set[str] | None
) -> int: ...
```



## convertStatic

[Show source in convert.py:62](../../../tstickers/convert.py#L62)

Convert static stickers to specified formats.

#### Arguments

- `swd` *Path* - The sticker working directory (e.g., downloads/packName).
- `threads` *int* - Number of threads for ProcessPoolExecutor (default: number of
logical processors).
:param set[str]|None formats: Set of formats to convert telegram webp stickers to
(default: {"gif", "png", "webp", "apng"})

#### Returns

Type: *int*
Number of stickers successfully converted.

#### Signature

```python
def convertStatic(
    swd: Path, threads: int = 4, formats: set[str] | None = None
) -> int: ...
```



## convertWithPIL

[Show source in convert.py:44](../../../tstickers/convert.py#L44)

Convert a webp file to specified formats.

#### Arguments

- `input_file` *Path* - path to the input image/ sticker
:param set[str] formats: set of formats

#### Returns

Type: *Path*
path of the original image/sticker file

#### Signature

```python
def convertWithPIL(input_file: Path, formats: set[str]) -> Path: ...
```