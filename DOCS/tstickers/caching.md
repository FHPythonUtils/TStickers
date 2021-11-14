# caching

> Auto-generated documentation for [tstickers.caching](../../tstickers/caching.py) module.

Sticker caching functionality used by the downloader.

- [Tstickers](../README.md#tstickers-index) / [Modules](../README.md#tstickers-modules) / [tstickers](index.md#tstickers) / caching
    - [createConverted](#createconverted)
    - [verifyConverted](#verifyconverted)

#### Attributes

- `cachedSession` - requests_cache: `CachedSession('.cache/tstickers.requests.sqlite...`

## createConverted

[[find in source code]](../../tstickers/caching.py#L60)

```python
def createConverted(packName: str, data: dict):
```

Write cache data to a file identified by packName

#### Arguments

- `packName` *str* - name of the sticker pack eg. "DonutTheDog"
- `data` *dict* - packName cache data to write to cache

## verifyConverted

[[find in source code]](../../tstickers/caching.py#L21)

```python
def verifyConverted(packName: str) -> bool:
```

Verify the cache for a packName eg. "DonutTheDog". Uses the cache "version"
to call the verify function for that version

#### Arguments

- `packName` *str* - name of the sticker pack eg. "DonutTheDog"

#### Returns

- `bool` - if the converted cache has been verified
