# animate

> Auto-generated documentation for [tstickers.animate](../../tstickers/animate.py) module.

- [Tstickers](../README.md#tstickers-index) / [Modules](../README.md#tstickers-modules) / [tstickers](index.md#tstickers) / animate
    - [convertTGS2GIF](#converttgs2gif)
    - [recordLottie](#recordlottie)

## convertTGS2GIF

[[find in source code]](../../tstickers/animate.py#L16)

```python
def convertTGS2GIF(fileName: str, newFileName: str):
```

Convert a tgs to gif

#### Arguments

- `fileName` *str* - file path of the tgs
- `newFileName` *str* - file path of the gif

## recordLottie

[[find in source code]](../../tstickers/animate.py#L34)

```python
async def recordLottie(lottieData: str) -> Tuple[(int, int)]:
```

Record the lottie data to a set of images

#### Arguments

- `lottieData` *str* - lottie data as string

#### Returns

- `Tuple[int,` *int]* - duration and number of frames
