# downloader

> Auto-generated documentation for [tstickers.downloader](../../tstickers/downloader.py) module.

Provides the module functions

- [Tstickers](../README.md#tstickers-index) / [Modules](../README.md#tstickers-modules) / [tstickers](index.md#tstickers) / downloader
    - [Sticker](#sticker)
        - [Sticker().emojiName](#stickeremojiname)
    - [StickerDownloader](#stickerdownloader)
        - [StickerDownloader().convertDir](#stickerdownloaderconvertdir)
        - [StickerDownloader().convertStatic](#stickerdownloaderconvertstatic)
        - [StickerDownloader().doAPIReq](#stickerdownloaderdoapireq)
        - [StickerDownloader().downloadSticker](#stickerdownloaderdownloadsticker)
        - [StickerDownloader().downloadStickerSet](#stickerdownloaderdownloadstickerset)
        - [StickerDownloader().getSticker](#stickerdownloadergetsticker)
        - [StickerDownloader().getStickerSet](#stickerdownloadergetstickerset)
    - [assureDirExists](#assuredirexists)

## Sticker

[[find in source code]](../../tstickers/downloader.py#L41)

```python
class Sticker():
    def __init__(
        name: str = 'None',
        link: str = 'None',
        emoji: str = '😀',
        animated: bool = False,
    ):
```

Sticker instance attributes

### Sticker().emojiName

[[find in source code]](../../tstickers/downloader.py#L55)

```python
def emojiName() -> str:
```

get the emoji as a string

## StickerDownloader

[[find in source code]](../../tstickers/downloader.py#L60)

```python
class StickerDownloader():
    def __init__(token, session=None, multithreading=4):
```

The StickerDownloader sets up the api and makes requests

### StickerDownloader().convertDir

[[find in source code]](../../tstickers/downloader.py#L222)

```python
def convertDir(name: str, frameSkip: int = 1, scale: float = 1):
```

Convert the webp images into png images

#### Arguments

- `name` *str* - name of the directory to convert
- `frameSkip` *int, optional* - skip n number of frames in the interest of
optimisation with a quality trade-off. Defaults to 1.
- `scale` *float, optional* - upscale/ downscale the images produced. Intended
for optimisation with a quality trade-off. Defaults to 1.

### StickerDownloader().convertStatic

[[find in source code]](../../tstickers/downloader.py#L205)

```python
def convertStatic(inputFile: str):
```

Convert the webp file to png

#### Arguments

- `inputFile` *str* - path to input file

### StickerDownloader().doAPIReq

[[find in source code]](../../tstickers/downloader.py#L79)

```python
def doAPIReq(
    function: str,
    params: dict[(Any, Any)],
) -> Optional[dict[(Any, Any)]]:
```

Use the telegram api

#### Arguments

- `function` *str* - function to execute
params (dict[Any, Any]): function parameters

#### Raises

- `RuntimeError` - In the event of a failure

#### Returns

- `Optional[dict[Any,` *Any]]* - api response

### StickerDownloader().downloadSticker

[[find in source code]](../../tstickers/downloader.py#L158)

```python
def downloadSticker(name: str, link: str, path: str) -> str:
```

Download a sticker from the server

#### Arguments

- `name` *str* - the name of the file
- `link` *str* - the url to the file on the server
- `path` *str* - the path to write to

#### Returns

- `str` - the filepath the file was written to

### StickerDownloader().downloadStickerSet

[[find in source code]](../../tstickers/downloader.py#L175)

```python
def downloadStickerSet(stickerSet: dict[(Any, Any)]):
```

Download sticker set.

### StickerDownloader().getSticker

[[find in source code]](../../tstickers/downloader.py#L105)

```python
def getSticker(fileData: dict[(Any, Any)]) -> Sticker:
```

Get sticker info from the server

#### Arguments

fileData (dict[Any, Any]): sticker id

#### Returns

- `Sticker` - Sticker instance

#### See also

- [Sticker](#sticker)

### StickerDownloader().getStickerSet

[[find in source code]](../../tstickers/downloader.py#L125)

```python
def getStickerSet(name: str) -> Optional[dict[(Any, Any)]]:
```

Get a list of File objects.

#### Arguments

- `name` *str* - name of the sticker set

#### Returns

- `dict[Any,` *Any]* - dictionary containing sticker data

## assureDirExists

[[find in source code]](../../tstickers/downloader.py#L22)

```python
def assureDirExists(directory: str, root: str) -> str:
```

make the dir if not exists

#### Arguments

- `directory` *str* - the directory name
- `root` *str* - the path of the root directory

#### Returns

- `str` - the full path
