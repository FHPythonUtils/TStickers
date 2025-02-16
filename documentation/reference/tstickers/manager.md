# Manager

[Tstickers Index](../README.md#tstickers-index) / [Tstickers](./index.md#tstickers) / Manager

> Auto-generated documentation for [tstickers.manager](../../../tstickers/manager.py) module.

- [Manager](#manager)
  - [Sticker](#sticker)
    - [Sticker().__repr__](#sticker()__repr__)
    - [Sticker().emojiName](#sticker()emojiname)
  - [StickerManager](#stickermanager)
    - [StickerManager().convertPack](#stickermanager()convertpack)
    - [StickerManager().doAPIReq](#stickermanager()doapireq)
    - [StickerManager().downloadPack](#stickermanager()downloadpack)
    - [StickerManager().downloadSticker](#stickermanager()downloadsticker)
    - [StickerManager().getPack](#stickermanager()getpack)
    - [StickerManager().getSticker](#stickermanager()getsticker)
  - [demojize](#demojize)

## Sticker

[Show source in manager.py:56](../../../tstickers/manager.py#L56)

Sticker instance attributes.

#### Signature

```python
class Sticker: ...
```

### Sticker().__repr__

[Show source in manager.py:64](../../../tstickers/manager.py#L64)

Get Sticker representation in the form <Sticker:name>.

#### Returns

Type: *str*
representation

#### Signature

```python
def __repr__(self) -> str: ...
```

### Sticker().emojiName

[Show source in manager.py:71](../../../tstickers/manager.py#L71)

Get the emoji as a string.

#### Signature

```python
def emojiName(self) -> str: ...
```



## StickerManager

[Show source in manager.py:76](../../../tstickers/manager.py#L76)

The StickerManager sets up the api and makes requests.

#### Signature

```python
class StickerManager:
    def __init__(
        self, token: str, session: caching.CachedSession | None = None, threads: int = 4
    ) -> None: ...
```

### StickerManager().convertPack

[Show source in manager.py:248](../../../tstickers/manager.py#L248)

Convert a downloaded sticker pack given by packName to other formats specified.

#### Arguments

- `packName` *str* - name of the pack to convert
- `fps` *int* - framerate of animated stickers, affecting optimization and
quality (default: 20)
- `scale` *float* - Scale factor of animated stickers, for up/downscaling images,
affecting optimization and quality (default: 1).
- `noCache` *bool* - set to true to disable cache. Defaults to False.
- `backend` *Backend* - select the backend to use to convert animated stickers
:param set[str]|None formats: Set of formats to convert telegram tgs stickers to
(default: {"gif", "webp", "apng"})

#### Signature

```python
def convertPack(
    self,
    packName: str,
    fps: int = 20,
    scale: float = 1,
    noCache: bool = False,
    backend: Backend = Backend.UNDEFINED,
    formats: set[str] | None = None,
) -> None: ...
```

#### See also

- [Backend](./convert.md#backend)

### StickerManager().doAPIReq

[Show source in manager.py:107](../../../tstickers/manager.py#L107)

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

### StickerManager().downloadPack

[Show source in manager.py:207](../../../tstickers/manager.py#L207)

Download a sticker pack.

#### Arguments

- `packName` *str* - name of the pack

#### Returns

Type: *bool*
success

#### Signature

```python
def downloadPack(self, packName: str) -> bool: ...
```

### StickerManager().downloadSticker

[Show source in manager.py:195](../../../tstickers/manager.py#L195)

Download a sticker from the server.

#### Arguments

- `path` *Path* - the path to write to
- `link` *str* - the url to the file on the server

#### Returns

Type: *int*
path.write_bytes(res.content)

#### Signature

```python
def downloadSticker(self, path: Path, link: str) -> int: ...
```

### StickerManager().getPack

[Show source in manager.py:161](../../../tstickers/manager.py#L161)

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

### StickerManager().getSticker

[Show source in manager.py:138](../../../tstickers/manager.py#L138)

Get sticker info from the server.

#### Arguments

----
 fileData (dict[str, Any]): sticker id

#### Returns

-------
 - [Sticker](#sticker) - Sticker instance

#### Signature

```python
def getSticker(self, fileData: dict[str, Any]) -> Sticker: ...
```

#### See also

- [Sticker](#sticker)



## demojize

[Show source in manager.py:22](../../../tstickers/manager.py#L22)

Similar to the emoji.demojize function.

However, returns a string of unique keywords in alphabetical order seperated by "_"

#### Arguments

- `emoji` *str* - emoji unicode char

#### Returns

Type: *str*
returns a string of unique keywords in alphabetical order seperated by "_"

#### Signature

```python
def demojize(emoji: str) -> str: ...
```