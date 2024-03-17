# Caching

[Tstickers Index](../README.md#tstickers-index) / [Tstickers](./index.md#tstickers) / Caching

> Auto-generated documentation for [tstickers.caching](../../../tstickers/caching.py) module.

#### Attributes

- `cachedSession` - requests_cache: CachedSession('.cache/tstickers.requests.sqlite', backend='sqlite', expire_after=60 * 60 * 12, allowable_codes=(200), allowable_methods=('GET', 'POST'))


- [Caching](#caching)
  - [_verifyConvertedV1](#_verifyconvertedv1)
  - [createConverted](#createconverted)
  - [verifyConverted](#verifyconverted)

## _verifyConvertedV1

[Show source in caching.py:47](../../../tstickers/caching.py#L47)

Verify the cache for a packName using cache data.

#### Arguments

----
 data (dict[str, Any]) packName cache data to verify

#### Returns

-------
 - `bool` - if the converted cache has been verified

#### Signature

```python
def _verifyConvertedV1(data: dict[str, Any]): ...
```



## createConverted

[Show source in caching.py:66](../../../tstickers/caching.py#L66)

Write cache data to a file identified by packName.

#### Arguments

----
 - `packName` *str* - name of the sticker pack eg. "DonutTheDog"
 - `data` *dict* - packName cache data to write to cache

#### Signature

```python
def createConverted(packName: str, data: dict) -> None: ...
```



## verifyConverted

[Show source in caching.py:21](../../../tstickers/caching.py#L21)

Verify the cache for a packName eg. "DonutTheDog". Uses the cache "version"
to call the verify function for that version.

#### Arguments

----
 - `packName` *str* - name of the sticker pack eg. "DonutTheDog"

#### Returns

-------
 - `bool` - if the converted cache has been verified

#### Signature

```python
def verifyConverted(packName: str) -> bool: ...
```