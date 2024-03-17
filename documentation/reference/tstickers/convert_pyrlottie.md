# Convert Pyrlottie

[Tstickers Index](../README.md#tstickers-index) / [Tstickers](./index.md#tstickers) / Convert Pyrlottie

> Auto-generated documentation for [tstickers.convert_pyrlottie](../../../tstickers/convert_pyrlottie.py) module.

- [Convert Pyrlottie](#convert-pyrlottie)
  - [convertAnimated](#convertanimated)

## convertAnimated

[Show source in convert_pyrlottie.py:8](../../../tstickers/convert_pyrlottie.py#L8)

Convert animated stickers to webp, gif and png.

#### Arguments

----
 - `swd` *Path* - the sticker working directory (downloads/packName)
 - `threads` *int, optional* - number of threads to pass to ThreadPoolExecutor. Defaults to 4.
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
    swd: Path, threads: int = 4, frameSkip: int = 1, scale: float = 1
) -> int: ...
```