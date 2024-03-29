# Rejected-PEPs Changelog

### <u>0.9.8 & 0.9.7</u>  _Final_

_Release Date: 2023-01-19_

#### New

- The register functions are backported from v1.0 in development. Examples:

  ```python
  >>> import rejected_peps as rp
  >>> rp.pep211.PEP
  211
  >>> rp.register(211, 'product')
  >>> rp.product.PEP
  211
  >>> rp.register(211, 'pd')
  >>> rp.pd.PEP
  211
  >>> rp.get('pd').PEP
  211
  >>> rp.unregister('pd')
  >>> rp.pd
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ...
  AttributeError: module 'rejected_peps' has no attribute 'pd'
  >>> rp.clear_register()
  >>> rp.product
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ...
  AttributeError: module 'rejected_peps' has no attribute 'product'
  ```

#### Fixed

- `pep249.apply` is now thread safe.
- `pep349.str`, `pep3140.str` and `pep349.str & pep3140.str` no longer raise `TypeError` if the argument is a type.

### <u>0.9.6</u>  _Final_

_Release Date: 2023-01-05_

#### Fixed

- `pep3140.str` and `pep349.str & pep3140.str` now correctly return the result for any mapping.

  For example:

  ```python
  >>> from collections import defaultdict as d
  >>> pep3140.str(d(int, {'1': 2}))
  {1: 2}  # v0.9.5
  defaultdict(<class 'int'>, {1: 2})  # v0.9.6
  ```

### <u>0.9.5</u>  _Final_

_Release Date: 2023-01-04_

#### Announcement

- Support for Python 3.8 is planned to be dropped on October 14, 2023; if you need extended support, please report it.

#### Fixed

- `pep351.freeze` now detects any sequence or mapping.
- `pep351.freeze(…, allow_frozendict=True)` no longer crashes if the `pep416` import fails.

### <u>0.9.4</u>  _Final_

_Release Date: 2023-01-04_

#### Improved

- Functions in `pep313` are now cached.

### <u>0.9.3</u>  _Final_

_Release Date: 2023-01-03_

#### Fixed

- Fix `test.run()`: it no longer exits when finished and can correctly run the tests in the module. You can override the non-exiting by specifying `exit=True`.

### <u>0.9.2</u>  _Final_

_Release Date: 2023-01-03_

#### Improved

- Functions in `__init__.py` are now cached.

### <u>0.9.1</u>  _Final_

_Release Date: 2023-01-03_

#### Improved

- Add tests for `__init__.py`.
- Functions in `pep313` now reject 0 if `pep336.isNone(zero)` instead of just checking for the builtin `None`.

### <u>0.9.0</u>  _Final_

_Release Date: 2023-01-02_

#### Breaking

- Remove `search_one` deprecated from v0.5; use `search.one` instead.

### <u>0.9.0</u>  _Beta 1_

_Release Date: 2023-01-01_

#### Improved

- `pep326.Min`, `pep326.Max` and `pep336.NoneType` can now be hashed.
- `DeprecationWarning` is now changed to `error`; `search_one` will be removed in v0.9.

### <u>0.8.2</u>  _Final_

_Release Date: 2023-01-01_

Happy New Year!

#### Improved

- `pep326.Min`, `pep326.Max` and `pep336.NoneType` can now be hashed.
- `DeprecationWarning` is now changed to `default`; `search_one` will be removed in v0.9.

### <u>0.9.0</u>  _Alpha 2_

_Release Date: 2022-12-30_

#### New

- [#7](https://github.com/wyz23x2/rejected-peps/issues/7), [#9](https://github.com/wyz23x2/rejected-peps/issues/9): You can now combine PEPs 204 & 281 and 212 & 281; use `r = pep204 & pep281.range` and `indices = pep212.indices & pep281.range`, or `rp.pep(204, 212, 281)` to get a namespace with `rliteral` for PEP 204 and `indices` for PEP 212. You cannot directly combine PEPs 204 and 212.

### <u>0.9.0</u>  _Alpha 1_

_Release Date: 2022-12-30_

#### New

- [#7](https://github.com/wyz23x2/rejected-peps/issues/7), [#8](https://github.com/wyz23x2/rejected-peps/issues/8): You can now combine PEPs 349 and 3140; use `rp.pep(349, 3140).str` or `str = pep349.str & pep3140.str` to let `str()` use `str()` on items and allow returning `bytes`.

### <u>0.8.1</u>  _Final_

_Release Date: 2022-12-29_

#### Improved

- [#6](https://github.com/wyz23x2/rejected-peps/issues/6): `pep349.str` is now also a class, supporting `isinstance` and `issubclass` checks. In these two contexts, it behaves the same as `builtins.str` _only_; hence, `isinstance('1', pep3140.str)` returns `True`. Note that `pep349.str(…)` returns a `builtins.str` or `builtins.bytes` instance, so it's compatible.
- [#6](https://github.com/wyz23x2/rejected-peps/issues/6): `pep349.str` now accepts the `str(bytes_or_buffer, encoding[, errors])` form; in these cases, it's interpreted as normal.

### <u>0.8.0</u>  _Final_

_Release Date: 2022-12-29_

#### Improved

- `pep204` no longer fails when imported if `pep211` is unavailable; however, `repr(pep204)` still fails if `pep211` is unavailable.


### <u>0.8.0</u>  _Candidate 1_

_Release Date: 2022-12-29_

#### Improved

- [#5](https://github.com/wyz23x2/rejected-peps/issues/5): `pep3140.str` now handles recursive objects correctly by replacing them with `…`, just as the builtin `str` does.

- `pep3140.str` is now a class, supporting `isinstance` and `issubclass` checks. In these two contexts, it behaves the same as `builtins.str`; hence, `isinstance('1', pep3140.str)` returns `True`. Note that `pep3140.str(…)` returns a `builtins.str` instance, so it's compatible.

### <u>0.8.0</u>  _Beta 2_

_Release Date: 2022-12-29_

#### Improved

- The order of the check for `__andfunc__` in `pep535.cmp` is adjusted; now in `A and B`, `A.__andfunc__` is checked before `B.__randfunc__`.
- The exception note is now added correctly in Python 3.11 when `AttributeError` is raised during the fallback in `pep535.cmp`.

### <u>0.8.0</u>  _Beta 1_

_Release Date: 2022-12-29_

#### New

- Add support of [PEP 535](https://peps.python.org/pep-0535/) — Rich comparison chaining.

### <u>0.7.2</u>  _Final_

_Release Date: 2022-12-29_

#### Improved

- `pep351.freeze` doesn't import `pep416` until needed (lazy import).
- Improve some error messages.

### <u>0.7.1</u>  _Final_

_Release Date: 2022-12-28_

#### Breaking

- Support for Python 3.6 is officially dropped. The `rejected_peps.pep204` format never worked since module `__getattr__` was not added until 3.7, and 3.6 entered EOL on Dec. 23, 2021. Support for Python 3.7 will be dropped starting from Jan. 27, 2023.

### <u>0.7.0</u>  _Final_

_Release Date: 2022-12-28_

#### Added

- Tests for PEPs 754 and 3140 are supported.

### <u>0.7.0</u>  _Candidate 1_

_Release Date: 2022-12-28_

#### Fixed

- `pep326.Min` is no longer less than itself; `pep326.Max` is no longer greater than itself.

### <u>0.7.0</u>  _Beta 1_

_Release Date: 2022-12-28_

#### New

- Tests for PEPs 204 to 559 are supported. Call `rp.run` to run the test suite.

#### Improved

- Update URLs in `info()` to the newest `peps.python.org` format.
- Add `file` parameter to `pep259.print()`.
- Correct the error messages of `pep303.divmod()`.
- Fix `pep303.rdivmod()`; the first argument is no longer touched.
- Add `PEP` constants to PEPs 259 and 313.
- Fix implementation of mode `modern` for 49+ in PEP 313.
- The parameter `allow_frozendict` of `pep351.freeze()` is keyword-only.
- `pep294.original(s)` and `pep294.underscore(s)` ensure that `s` is a `str`.

### <u>0.6.1</u>  _Final_

_Release Date: 2021-08-22_

#### Fixed

- Fix a possible `UnboundLocalError` in `pep294.apply()`.

#### Improved

- `to_roman(x)` now checks for `x.__index__` before falling back to `int(x)` & `int(x, 0)`.

### <u>0.6.0</u>  _Final_

_Release Date: 2021-08-22_

#### Removed

- `roman()`, `to_int()` and `zero` deprecated for 5 versions in [PEP 313](https://www.python.org/dev/peps/pep-0313/) are removed. They were replaced by `to_roman()`, `from_roman()` and `default_zero` in v0.4.1.

### <u>0.6.0</u>  _Candidate 2_

_Release Date: 2021-08-22_

#### Improved

- 3 leading underscores are now accepted in `pep313.large_dict`, e.g. `___D` → 500,000,000,000.

#### Fixed

- Correct a typo in the [PEP 335](https://www.python.org/dev/peps/pep-0335/) warning message.
- Raise `TypeError` early in `print()` of [PEP 259](https://www.python.org/dev/peps/pep-0259/) when `end` is not `None` or a `str` to prevent unhelpful messages for `str.startswith` and incorrect usage of non str-subclass `startswith` methods.

### <u>0.6.0</u>  _Candidate 1_

_Release Date: 2021-08-22_

#### Breaking

- The [PEP 294](https://www.python.org/dev/peps/pep-0294/) implementation is rewritten.
	- Importing `pep294` no longer directly sets attributes of the `types` module. The original behavior is fragile, surprising and requires `importlib.reload(pep294)` to rerun the code.
	- Instead, the `apply(module=None, *, rename=pep294.underscore, strict=None)` function is added. [^1]  
		- `module` defaults to `types` when it's `None`, otherwise attributes of it are set. 
		- `rename` is a function that handles invalid names (i.e. a keyword or not an identifier). For example, `LambdaType` is converted to `lambda`, which is invalid. `rename(name)` returns the new variant.
		- `strict` is a `bool` or `None`. If `strict` is `None`, it is `False` if `rename` is `pep294.original`, else `True`. If it's true and the new name is not a `str` or invalid, `TypeError` or `ValueError` is raised depending on the error. `rename` is _always_ called before checking.
		- This function returns `None` since it is an in-place operation on `module`.
	- The `underscore(s)`, `title(s)` and `original(s)` functions are for the `rename` parameter.
		- `underscore` appends an underscore (`_`) to the name. For example, `lambda` → `lambda_`. This is the default value.
		- `title` is an alias of `str.title`. For example, `lambda` → `Lambda`.
		- `original` just returns the name unchanged. This is usually used when attributes aren't meant to be accessed by the `types.x` syntax, but `getattr(types, 'x')` etc. 

#### Improved

- `DeprecationWarning` is now issued instead of `Warning` in [PEP 335](https://www.python.org/dev/peps/pep-0335/) if `NotImplemented` is returned. This matches the behavior starting from Python 3.9, and allows controlling it without effecting other `Warning` subclasses.
- Since it's a singleton, `hash(pep335.NeedOtherOperand)` now returns the hash of it's ID, rather than the fixed value 9223363241139.

#### Deprecated

- The filter action of `DeprecationWarning` is now turned to `always` since old names in `pep313` were deprecated in v0.4.1 and removal is scheduled on v0.6. `roman()`, `to_int()` and `zero` will be removed in v0.6.0 final. Please make sure you use the new names `to_roman()`, `from_roman()` and `default_zero`.

#### Fixed

- The Python `DeprecationWarning` is now silenced in `pep335` since it's already issued manually. Note that `DeprecationWarning` in `NOT(NotImplemented)` is still the builtin one.

[^1]: There is a built-in `apply()` function in Python 2.x, but anyway we didn't support 2.x from the start, and `apply` is just a name, not a keyword.

### <u>0.5.0</u>  _Final_

_Release Date: 2021-08-11_

#### New

- Add support of [PEP 335](https://www.python.org/dev/peps/pep-0335/) — Overloadable Boolean ~~Operators~~ Operator Functions.
- The new `search.one` is now preferred over `search_one`.
- Add `search.any` and `search.one.any` to match titles that contain _any_ of the arguments. The default behavior is still _all_ of them.

### <u>0.4.2</u>  _Final_

_Release Date: 2021-08-11_

#### New

- Rejected-PEPs is now typed! See [PEP 484](https://www.python.org/dev/peps/pep-0484/) for more information about typing.

#### Improved

- `info()` now raises `rejected_peps.UnavailableError` if a PEP is supported but info is unavailable. It is a subclass of `NotImplementedError` and `LookupError`, so previous code catching `NotImplementedError` won't break.
- Improve some documentation to be clearer.


### <u>0.4.1</u>  _Final_

_Release Date: 2021-08-09_

#### Breaking

- The support of [PEP 313](https://www.python.org/dev/peps/pep-0313/) has underwent some major changes.
  - `roman()` is renamed to `to_roman()`. The original name is deprecated and will be removed in v0.6.
  - `to_int()` is renamed to `from_roman()`. The original name is deprecated and will be removed in v0.6.
  - `zero` is renamed to `default_zero`. The original name is deprecated and will be removed in v0.6.
  - `from_roman()` now supports parsing roman fractions.

#### Improved

- A minor cleanup was done for some files (removing unneeded imports etc.).

### <u>0.4.0</u>  _Final_

_Release Date: 2021-08-09_

#### New

- Add support of [PEP 313](https://www.python.org/dev/peps/pep-0313/) — Adding Roman Numeral ~~Literals~~ Functions to Python
- Add functions `search(*s, strict=False)`, `search_one(*s, strict=True)` and `get(*s)`.


### <u>0.3.1</u>  _Final_

_Release Date: 2021-08-08_

#### New

- Add support of:
	- [PEP 294](https://www.python.org/dev/peps/pep-0294/) — Type Names in the types Module
	- [PEP 754](https://www.python.org/dev/peps/pep-0754/) — IEEE 754 Floating Point Special Values

### <u>0.3.0</u>  _Final_

_Release Date: 2021-08-08_

#### New

- Add support of [PEP 281](https://www.python.org/dev/peps/pep-0281/) — Loop Counter Iteration with `range` ~~and `xrange`~~

#### Fixed
- Add 259 into `SUPPORTED`

### <u>0.2.4</u>  _Final_

_Release Date: 2021-08-08_

#### New

- Add support of [PEP 259](https://www.python.org/dev/peps/pep-0259/) — Omit printing newline after newline

#### Fixed

- Add the missing `PEP` constant in `pep204`.


### <u>0.2.3</u>  _Final_

_Release Date: 2021-08-08_

#### New

- Add support of [PEP 204](https://www.python.org/dev/peps/pep-0204/) — Range Literals

#### Improved

- `pep3140.str()` now correctly formats mappings, not just `dict`.

### <u>0.2.2</u>  _Final_

_Release Date: 2021-08-08_

#### New

- Add support of [PEP 3140](https://www.python.org/dev/peps/pep-3140/) – `str(container)` should call `str(item)`, not `repr(item)`.

### <u>0.2.1</u>  _Final_

_Release Date: 2021-08-08_

**This is the first version guaranteed having no install or import problems in regular environments.**

#### Fixes

- Fix `dir(rejected_peps)`.
- Fix module raising `ValueError` when directly run.

### <u>0.2.0</u>  _Final_

_Release Date: 2021-08-08_

#### New

- `dir(rejected_peps)` now includes the pep submodule names.

### <u>0.2.0</u>  _Beta 3_

_Release Date: 2021-08-08_

#### Fixes

- Fix submodule not being found.

### <u>0.2.0</u>  _Beta 2_

_Release Date: 2021-08-08_

#### New

- Add support of:
	- [PEP 211](https://www.python.org/dev/peps/pep-0211/) — Adding A New Outer Product Operator
	- [PEP 336](https://www.python.org/dev/peps/pep-0336/) — Make `None` callable
	- [PEP 349](https://www.python.org/dev/peps/pep-0349/) — Allow `str()` to return ~~unicode strings~~ bytes

#### Fixes

- Fix self-inheriting bug in PEP 276.

### <u>0.2.0</u>  _Beta 1_

_Release Date: 2021-08-08_

#### Fixes

- Fix all installing and importing problems of 0.1.0.

### <u>0.1.0</u>  _Final_

_Release Date: 2021-08-08_

Initial release!

