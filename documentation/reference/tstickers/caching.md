# Caching

[Tstickers Index](../README.md#tstickers-index) /
[Tstickers](./index.md#tstickers) /
Caching

> Auto-generated documentation for [tstickers.caching](../../../tstickers/caching.py) module.

#### Attributes

- `cachedSession` - requests_cache: `CachedSession('.cache/tstickers.requests.sqlite', backend='sqlite', expire_after=60 * 60 * 12, allowable_codes=(200), allowable_methods=('GET', 'POST'))`


- [Caching](#caching)
  - [createConverted](#createconverted)
  - [verifyConverted](#verifyconverted)

## createConverted

[Show source in caching.py:60](../../../tstickers/caching.py#L60)

Write cache data to a file identified by packName

#### Arguments

- `packName` *str* - name of the sticker pack eg. "DonutTheDog"
- `data` *dict* - packName cache data to write to cache

#### Signature

```python
def createConverted(packName: str, data: dict):
    ...
```



## verifyConverted

[Show source in caching.py:21](../../../tstickers/caching.py#L21)

Verify the cache for a packName eg. "DonutTheDog". Uses the cache "version"
to call the verify function for that version

#### Arguments

- `packName` *str* - name of the sticker pack eg. "DonutTheDog"

#### Returns

- `bool` - if the converted cache has been verified

#### Signature

```python
def verifyConverted(packName: str) -> bool:
    ...
```


