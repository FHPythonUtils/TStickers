# Downloader

[Tstickers Index](../README.md#tstickers-index) / [Tstickers](./index.md#tstickers) / Downloader

> Auto-generated documentation for [tstickers.downloader](../../../tstickers/downloader.py) module.

- [Downloader](#downloader)
  - [Sticker](#sticker)
    - [Sticker().emojiName](#sticker()emojiname)
  - [StickerDownloader](#stickerdownloader)
    - [StickerDownloader().convertPack](#stickerdownloader()convertpack)
    - [StickerDownloader().doAPIReq](#stickerdownloader()doapireq)
    - [StickerDownloader().downloadPack](#stickerdownloader()downloadpack)
    - [StickerDownloader().downloadSticker](#stickerdownloader()downloadsticker)
    - [StickerDownloader().getPack](#stickerdownloader()getpack)
    - [StickerDownloader().getSticker](#stickerdownloader()getsticker)

## Sticker

[Show source in downloader.py:20](../../../tstickers/downloader.py#L20)

Sticker instance attributes.

#### Signature

```python
class Sticker:
    def __init__(
        self,
        name: str = "None",
        link: str = "None",
        emoji: str = "😀",
        fileType: str = "webp",
    ) -> None: ...
```

### Sticker().emojiName

[Show source in downloader.py:38](../../../tstickers/downloader.py#L38)

Get the emoji as a string.

#### Signature

```python
def emojiName(self) -> str: ...
```



## StickerDownloader

[Show source in downloader.py:43](../../../tstickers/downloader.py#L43)

The StickerDownloader sets up the api and makes requests.

#### Signature

```python
class StickerDownloader:
    def __init__(
        self,
        token: str,
        session: caching.CachedSession | None = None,
        multithreading: int = 4,
    ) -> None: ...
```

### StickerDownloader().convertPack

[Show source in downloader.py:205](../../../tstickers/downloader.py#L205)

Convert the webp to gif and png; tgs to gif, webp (webp_animated) and png.

#### Arguments

----
 - `packName` *str* - name of the directory to convert
 - `frameSkip` *int, optional* - skip n number of frames in the interest of
 optimisation with a quality trade-off. Defaults to 1.
 - `scale` *float, optional* - upscale/ downscale the images produced. Intended
 for optimisation with a quality trade-off. Defaults to 1.
 - `noCache` *bool, optional* - set to true to disable cache. Defaults to False.

#### Signature

```python
def convertPack(
    self,
    packName: str,
    frameSkip: int = 1,
    scale: float = 1,
    noCache: bool = False,
    backend: Backend = Backend.UNDEFINED,
) -> None: ...
```

#### See also

- [Backend](./convert.md#backend)

### StickerDownloader().doAPIReq

[Show source in downloader.py:64](../../../tstickers/downloader.py#L64)

Use the telegram api.

#### Arguments

----
 - `function` *str* - function to execute
 params (dict[Any, Any]): function parameters

#### Raises

------
 - `RuntimeError` - In the event of a failure

#### Returns

-------
 - `Optional[dict[Any,` *Any]]* - api response

#### Signature

```python
def doAPIReq(self, function: str, params: dict[Any, Any]) -> dict[Any, Any] | None: ...
```

### StickerDownloader().downloadPack

[Show source in downloader.py:167](../../../tstickers/downloader.py#L167)

Download a sticker pack.

#### Arguments

----
 pack (dict[str, Any]): dictionary representing a sticker pack

#### Returns

-------
 - `bool` - success

#### Signature

```python
def downloadPack(self, pack: dict[str, Any]) -> bool: ...
```

### StickerDownloader().downloadSticker

[Show source in downloader.py:152](../../../tstickers/downloader.py#L152)

Download a sticker from the server.

#### Arguments

----
 - `path` *Path* - the path to write to
 - `link` *str* - the url to the file on the server

#### Returns

-------
 - `int` - path.write_bytes(res.content)

#### Signature

```python
def downloadSticker(self, path: Path, link: str) -> int: ...
```

### StickerDownloader().getPack

[Show source in downloader.py:118](../../../tstickers/downloader.py#L118)

Get a list of File objects.

#### Arguments

----
 - `packName` *str* - name of the pack

#### Returns

-------
 - `dict[str,` *Any]* - dictionary containing sticker data

#### Signature

```python
def getPack(self, packName: str) -> dict[str, Any] | None: ...
```

### StickerDownloader().getSticker

[Show source in downloader.py:95](../../../tstickers/downloader.py#L95)

Get sticker info from the server.

#### Arguments

----
 fileData (dict[Any, Any]): sticker id

#### Returns

-------
 - [Sticker](#sticker) - Sticker instance

#### Signature

```python
def getSticker(self, fileData: dict[Any, Any]) -> Sticker: ...
```

#### See also

- [Sticker](#sticker)