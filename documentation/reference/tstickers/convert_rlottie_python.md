# Convert Rlottie Python

[Tstickers Index](../README.md#tstickers-index) / [Tstickers](./index.md#tstickers) / Convert Rlottie Python

> Auto-generated documentation for [tstickers.convert_rlottie_python](../../../tstickers/convert_rlottie_python.py) module.

- [Convert Rlottie Python](#convert-rlottie-python)
  - [convertAnimated](#convertanimated)
  - [convert_single_tgs](#convert_single_tgs)

## convertAnimated

[Show source in convert_rlottie_python.py:49](../../../tstickers/convert_rlottie_python.py#L49)

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
) -> int: ...
```



## convert_single_tgs

[Show source in convert_rlottie_python.py:26](../../../tstickers/convert_rlottie_python.py#L26)

#### Signature

```python
def convert_single_tgs(stckr: Path, fps: int, scale: float = 1.0) -> int: ...
```