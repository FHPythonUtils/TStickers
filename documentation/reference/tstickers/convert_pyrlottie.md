# Convert Pyrlottie

[Tstickers Index](../README.md#tstickers-index) / [Tstickers](./index.md#tstickers) / Convert Pyrlottie

> Auto-generated documentation for [tstickers.convert_pyrlottie](../../../tstickers/convert_pyrlottie.py) module.

- [Convert Pyrlottie](#convert-pyrlottie)
  - [convertAnimated](#convertanimated)

## convertAnimated

[Show source in convert_pyrlottie.py:17](../../../tstickers/convert_pyrlottie.py#L17)

Convert animated stickers, over a number of threads, at a given framerate, scale and to a
set of formats.

#### Arguments

- `swd` *Path* - The sticker working directory (e.g., downloads/packName).
- `_threads` *int* - This is ignored for the pyrlottie backend
- `fps` *int* - framerate of the converted sticker, affecting optimization and
quality (default: 20)
- `scale` *float* - Scale factor for up/downscaling images, affecting optimization and
quality (default: 1).
:param set[str] | None _formats: This is ignored for the pyrlottie backend

#### Returns

Type: *int*
Number of stickers successfully converted.

#### Signature

```python
def convertAnimated(
    swd: Path,
    _threads: int = 4,
    fps: int = 20,
    scale: float = 1,
    _formats: set[str] | None = None,
) -> int: ...
```