# animate

> Auto-generated documentation for [tstickers.animate](../../tstickers/animate.py) module.

- [Tstickers](../README.md#tstickers-index) / [Modules](../README.md#tstickers-modules) / [tstickers](index.md#tstickers) / animate
    - [convertTGS2GIF](#converttgs2gif)
    - [convertTGS2PIL](#converttgs2pil)
    - [convertTGS2Webp](#converttgs2webp)
    - [recordLottie](#recordlottie)

## convertTGS2GIF

[[find in source code]](../../tstickers/animate.py#L32)

```python
def convertTGS2GIF(
    images: List[Image.Image],
    duration: float,
    newFileName: str,
):
```

Convert to gif

#### Arguments

- `images` *List[Image.Image]* - list of pil images to write
- `duration` *float* - duration of the gif
- `newFileName` *str* - name of the file to write

## convertTGS2PIL

[[find in source code]](../../tstickers/animate.py#L14)

```python
def convertTGS2PIL(fileName: str) -> Tuple[(List[Image.Image], float)]:
```

Convert a tgs to gif

#### Arguments

- `fileName` *str* - file path of the tgs

#### Returns

- `Tuple[List[Image.Image],` *float]* - pil images to write to gif/ webp and duration

## convertTGS2Webp

[[find in source code]](../../tstickers/animate.py#L43)

```python
def convertTGS2Webp(images: Image.Image, duration: float, newFileName: str):
```

## recordLottie

[[find in source code]](../../tstickers/animate.py#L48)

```python
async def recordLottie(lottieData: str) -> Tuple[(int, int)]:
```

Record the lottie data to a set of images

#### Arguments

- `lottieData` *str* - lottie data as string

#### Returns

- `Tuple[int,` *int]* - duration and number of frames
