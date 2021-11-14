# downloader

> Auto-generated documentation for [tstickers.downloader](../../tstickers/downloader.py) module.

Sticker download functions used by the module entry point.

- [Tstickers](../README.md#tstickers-index) / [Modules](../README.md#tstickers-modules) / [tstickers](index.md#tstickers) / downloader
    - [Sticker](#sticker)
        - [Sticker().emojiName](#stickeremojiname)
    - [StickerDownloader](#stickerdownloader)
        - [StickerDownloader().convertPack](#stickerdownloaderconvertpack)
        - [StickerDownloader().doAPIReq](#stickerdownloaderdoapireq)
        - [StickerDownloader().downloadPack](#stickerdownloaderdownloadpack)
        - [StickerDownloader().downloadSticker](#stickerdownloaderdownloadsticker)
        - [StickerDownloader().getPack](#stickerdownloadergetpack)
        - [StickerDownloader().getSticker](#stickerdownloadergetsticker)
    - [assureDirExists](#assuredirexists)

## Sticker

[[find in source code]](../../tstickers/downloader.py#L40)

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

[[find in source code]](../../tstickers/downloader.py#L54)

```python
def emojiName() -> str:
```

get the emoji as a string

## StickerDownloader

[[find in source code]](../../tstickers/downloader.py#L59)

```python
class StickerDownloader():
    def __init__(token, session=None, multithreading=4):
```

The StickerDownloader sets up the api and makes requests

### StickerDownloader().convertPack

[[find in source code]](../../tstickers/downloader.py#L212)

```python
def convertPack(packName: str, frameSkip: int = 1, scale: float = 1):
```

Convert the webp to gif and png; tgs to gif, webp (webp_animated) and png.

#### Arguments

- `packName` *str* - name of the directory to convert
- `frameSkip` *int, optional* - skip n number of frames in the interest of
optimisation with a quality trade-off. Defaults to 1.
- `scale` *float, optional* - upscale/ downscale the images produced. Intended
for optimisation with a quality trade-off. Defaults to 1.

### StickerDownloader().doAPIReq

[[find in source code]](../../tstickers/downloader.py#L78)

```python
def doAPIReq(
    function: str,
    params: dict[(Any, Any)],
) -> dict[(Any, Any)] | None:
```

Use the telegram api

#### Arguments

- `function` *str* - function to execute
params (dict[Any, Any]): function parameters

#### Raises

- `RuntimeError` - In the event of a failure

#### Returns

- `Optional[dict[Any,` *Any]]* - api response

### StickerDownloader().downloadPack

[[find in source code]](../../tstickers/downloader.py#L174)

```python
def downloadPack(pack: dict[(str, Any)]) -> list[str]:
```

Download a sticker pack.

#### Arguments

pack (dict[str, Any]): dictionary representing a sticker pack

#### Returns

- `list[str]` - list of file paths each sticker is written to

### StickerDownloader().downloadSticker

[[find in source code]](../../tstickers/downloader.py#L157)

```python
def downloadSticker(name: str, link: str, path: str) -> str:
```

Download a sticker from the server.

#### Arguments

- `name` *str* - the name of the file
- `link` *str* - the url to the file on the server
- `path` *str* - the path to write to

#### Returns

- `str` - the filepath the file is written to

### StickerDownloader().getPack

[[find in source code]](../../tstickers/downloader.py#L124)

```python
def getPack(packName: str) -> dict[(str, Any)] | None:
```

Get a list of File objects.

#### Arguments

- `packName` *str* - name of the pack

#### Returns

- `dict[str,` *Any]* - dictionary containing sticker data

### StickerDownloader().getSticker

[[find in source code]](../../tstickers/downloader.py#L104)

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

## assureDirExists

[[find in source code]](../../tstickers/downloader.py#L21)

```python
def assureDirExists(directory: str, root: str) -> str:
```

make the dir if not exists

#### Arguments

- `directory` *str* - the directory name
- `root` *str* - the path of the root directory

#### Returns

- `str` - the full path
