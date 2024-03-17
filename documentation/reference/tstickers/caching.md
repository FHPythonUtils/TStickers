# Caching

[Tstickers Index](../README.md#tstickers-index) / [Tstickers](./index.md#tstickers) / Caching

> Auto-generated documentation for [tstickers.caching](../../../tstickers/caching.py) module.

#### Attributes

- `cachedSession` - requests_cache: CachedSession('.cache/tstickers.requests.sqlite', backend='sqlite', expire_after=60 * 60 * 12, allowable_codes=(200), allowable_methods=('GET', 'POST'))


- [Caching](#caching)
  - [_get_verify_function](#_get_verify_function)
  - [_verify_converted_v1](#_verify_converted_v1)
  - [create_converted](#create_converted)
  - [verify_converted](#verify_converted)

## _get_verify_function

[Show source in caching.py:83](../../../tstickers/caching.py#L83)

Get the appropriate cache verification function based on version.

#### Arguments

----
 - `version` *int* - Cache version

#### Returns

-------
 Callable[[dict[str, Any]], bool]: Cache verification function

#### Signature

```python
def _get_verify_function(version: int) -> Callable[[dict[str, Any]], bool]: ...
```



## _verify_converted_v1

[Show source in caching.py:51](../../../tstickers/caching.py#L51)

Verify the cache for a packName using cache data.

#### Arguments

----
 data (dict[Path, Any]): packName cache data to verify

#### Returns

-------
 - `bool` - if the converted cache has been verified

#### Signature

```python
def _verify_converted_v1(data: dict[str, Any]) -> bool: ...
```



## create_converted

[Show source in caching.py:70](../../../tstickers/caching.py#L70)

Write cache data to a file identified by packName.

#### Arguments

----
 - `pack_name` *str* - name of the sticker pack eg. "DonutTheDog"
 - `data` *dict* - packName cache data to write to cache

#### Signature

```python
def create_converted(pack_name: str, data: dict) -> None: ...
```



## verify_converted

[Show source in caching.py:27](../../../tstickers/caching.py#L27)

Verify the cache for a packName eg. "DonutTheDog". Uses the cache "version"
to call the verify function for that version.

#### Arguments

----
 - `pack_name` *str* - name of the sticker pack eg. "DonutTheDog"

#### Returns

-------
 - `bool` - if the converted cache has been verified

#### Signature

```python
def verify_converted(pack_name: str) -> bool: ...
```