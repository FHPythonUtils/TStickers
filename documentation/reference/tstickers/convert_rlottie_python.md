# Convert Rlottie Python

[Tstickers Index](../README.md#tstickers-index) / [Tstickers](./index.md#tstickers) / Convert Rlottie Python

> Auto-generated documentation for [tstickers.convert_rlottie_python](../../../tstickers/convert_rlottie_python.py) module.

- [Convert Rlottie Python](#convert-rlottie-python)
  - [convertAnimated](#convertanimated)
  - [convert_single_tgs](#convert_single_tgs)

## convertAnimated

[Show source in convert_rlottie_python.py:59](../../../tstickers/convert_rlottie_python.py#L59)

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
    formats: set[str] | None = None,
) -> int: ...
```



## convert_single_tgs

[Show source in convert_rlottie_python.py:18](../../../tstickers/convert_rlottie_python.py#L18)

Convert a single tgs file.

#### Arguments

- `stckr` *Path* - Path to the sticker
- `fps` *int* - framerate of the converted sticker, affecting optimization and
quality (default: 20)
- `scale` *float* - Scale factor for up/downscaling images, affecting optimization and
quality (default: 1).
:param set[str]|None formats: Set of formats to convert telegram tgs stickers to
(default: {"gif", "webp", "apng"})

#### Returns

Type: *int*
1 if success

#### Signature

```python
def convert_single_tgs(
    stckr: Path, fps: int, scale: float = 1.0, formats: set[str] | None = None
) -> int: ...
```