# downloader

> Auto-generated documentation for [tstickers.downloader](../../tstickers/downloader.py) module.

- [Tstickers](../README.md#tstickers-index) / [Modules](../README.md#tstickers-modules) / [tstickers](index.md#tstickers) / downloader
    - [File](#file)
    - [StickerDownloader](#stickerdownloader)
        - [StickerDownloader().convertDir](#stickerdownloaderconvertdir)
        - [StickerDownloader().convertStatic](#stickerdownloaderconvertstatic)
        - [StickerDownloader().doAPIReq](#stickerdownloaderdoapireq)
        - [StickerDownloader().downloadFile](#stickerdownloaderdownloadfile)
        - [StickerDownloader().downloadStickerSet](#stickerdownloaderdownloadstickerset)
        - [StickerDownloader().getFile](#stickerdownloadergetfile)
        - [StickerDownloader().getStickerSet](#stickerdownloadergetstickerset)
    - [assureDirExists](#assuredirexists)

## File

[[find in source code]](../../tstickers/downloader.py#L38)

```python
class File():
    def __init__(name: str, link: str):
```

File container has name and a link

## StickerDownloader

[[find in source code]](../../tstickers/downloader.py#L49)

```python
class StickerDownloader():
    def __init__(token, session=None, multithreading=4):
```

The StickerDownloader sets up the api and makes requests

### StickerDownloader().convertDir

[[find in source code]](../../tstickers/downloader.py#L206)

```python
def convertDir(name: str, quality: int = 1):
```

Convert the webp images into png images

#### Arguments

- `name` *str* - name of the directory to convert
- `quality` *int* - quality of animated images. Default=1

### StickerDownloader().convertStatic

[[find in source code]](../../tstickers/downloader.py#L188)

```python
def convertStatic(inputFile: str):
```

Convert the webp file to png

#### Arguments

- `inputFile` *str* - path to input file

#### Returns

None

### StickerDownloader().doAPIReq

[[find in source code]](../../tstickers/downloader.py#L69)

```python
def doAPIReq(
    fstring: str,
    params: dict[(Any, Any)],
) -> Optional[dict[(Any, Any)]]:
```

general method call

### StickerDownloader().downloadFile

[[find in source code]](../../tstickers/downloader.py#L147)

```python
def downloadFile(name: str, link: str, path: str) -> str:
```

Download a file from the server

#### Arguments

- `name` *str* - the name of the file
- `link` *str* - the url to the file on the server
- `path` *str* - the path

#### Returns

- `str` - the filepath the file was written to

### StickerDownloader().downloadStickerSet

[[find in source code]](../../tstickers/downloader.py#L164)

```python
def downloadStickerSet(stickerSet: dict[(Any, Any)]):
```

Download sticker set.

### StickerDownloader().getFile

[[find in source code]](../../tstickers/downloader.py#L91)

```python
def getFile(fileId: str) -> File:
```

Get the file from the server

#### Arguments

- `fileId` *str* - sticker id

#### Returns

- `File` - [description]

#### See also

- [File](#file)

### StickerDownloader().getStickerSet

[[find in source code]](../../tstickers/downloader.py#L110)

```python
def getStickerSet(name: str) -> Optional[dict[(Any, Any)]]:
```

Get a list of File objects.

#### Arguments

- `name` *str* - name of the sticker set

#### Returns

- `dict[Any,` *Any]* - dictionary containing sticker data

## assureDirExists

[[find in source code]](../../tstickers/downloader.py#L19)

```python
def assureDirExists(directory: str, root: str) -> str:
```

make the dir if not exists

#### Arguments

- `dir` *str* - the directory name
- `root` *str* - the path of the root directory

#### Returns

- `str` - the full path
