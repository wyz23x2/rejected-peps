<!-- Changes in v1.0a1 that will not backport to v0.9 and are not related to tests or documentation -->
- The default value of the `sortby` parameter in `pep265.itemlist` will become `VALUES` instead of `ORIGINAL` in future versions; not specifying it now issues a `DeprecationWarning`.
- `pep294.apply()` is now thread safe and returns the modified module.
- `pep294.apply()` now uses `importlib.import_module` instead of `__import__`.
- `pep211.wrapper` now gains a `__wrapped__` property storing the object, same as `__call__()`.
- `pep211.wrapper` now supports `w @ n` where `w` is a `wrapper` and `n` is an `int`. In this case `w @ n` is the same as `itertools.product(w(), repeat=n)`.
