<!-- Changes in v1.0a1 that will not backport to v0.9 and are not related to tests or documentation -->
- The default value of the `sortby` parameter in `pep265.itemlist` will become `VALUES` instead of `ORIGINAL` in future versions; not specifying it now issues a `DeprecationWarning`.

- `pep294.apply()` now returns the modified module.

- `pep294.apply()` now uses `importlib.import_module` instead of `__import__`.

- `pep294.apply()` now accepts a keyword-only argument `mapfunc` (default `original`); every _new_ name will be passed to `mapfunc` and the valid check will be done with the new name.

  Note that names that originally do _not_ end with `Type` will also be processed, _but_ names that end with `Type` only after `mapfunc` is called will _not_ be further touched; check for the prefix `Type` if you only want changed names to be processed.

  Basic pseudo code:

  ```python
  new_name = mapfunc(old_name)
  if old_name.endswith("Type"):
      if not valid(new_name):
          new_name = rename(new_name)
          if strict and not valid(new_name):
              raise ValueError(f'Invalid name {new_name!r}')
          # set attribute of module
  ```

- `pep211.wrapper` gains a `__wrapped__` property storing the object, same as `__call__()`.

- `pep211.wrapper` now supports `w @ n` where `w` is a `wrapper` and `n` is an `int`. In this case `w @ n` is the same as `itertools.product(w(), repeat=n)`.

- pip wheels for Windows are now supported.
