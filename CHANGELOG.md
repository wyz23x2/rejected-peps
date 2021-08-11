# Rejected-PEPs Changelog

### <u>0.5.0</u>  _Final_

_Release Date: 2021-08-11_

#### New

- Add support of [PEP 335](https://python.org/dev/peps/pep-0335/) — Overloadable Boolean ~~Operators~~ Operator Functions
- The new `search.one` is now preferred over `search_one`.
- Added `search.any` and `search.one.any` to match titles that contain _any_ of the arguments. The default behavior is still _all_ of them.

### <u>0.4.2</u>  _Final_

_Release Date: 2021-08-11_

#### New

- Rejected-PEPs is now typed! See [PEP 484](https://python.org/dev/peps/pep-0484.html) for more information about typing.

#### Improved

- `info()` now raises `rejected_peps.UnavailableError` if a PEP is supported but info is unavailable. It is a subclass of `NotImplementedError` and `LookupError`, so previous code catching `NotImplementedError` won't break.
- Improve some documentation to be clearer.


### <u>0.4.1</u>  _Final_

_Release Date: 2021-08-09_

#### Improved

- The support of [PEP 313](https://python.org/dev/peps/pep-0313/) has underwent some major changes.
  - **BREAKING**  `roman()` has been renamed to `to_roman()`. The original name is deprecated and will be removed in v0.6.
  - **BREAKING**  `to_int()` has been renamed to `from_roman()`. The original name is deprecated and will be removed in v0.6.
  - **BREAKING** `zero` has been renamed to `default_zero`. The original name is deprecated and will be removed in v0.6.
  - `from_roman()` now supports parsing roman fractions.
- A minor cleanup was done for some files (removing unneeded imports etc.).

### <u>0.4.0</u>  _Final_

_Release Date: 2021-08-09_

#### New

- Add support of [PEP 313](https://python.org/dev/peps/pep-0313/) — Adding Roman Numeral ~~Literals~~ Functions to Python
- Add functions `search(*s, strict=False)`, `search_one(*s, strict=True)` and `get(*s)`.


### <u>0.3.1</u>  _Final_

_Release Date: 2021-08-08_

#### New

- Add support of:
	- [PEP 294](https://python.org/dev/peps/pep-0294/) — Type Names in the types Module
	- [PEP 754](https://python.org/dev/peps/pep-0754/) — IEEE 754 Floating Point Special Values

### <u>0.3.0</u>  _Final_

_Release Date: 2021-08-08_

#### New

- Add support of [PEP 281](https://www.python.org/dev/peps/pep-0281/) — Loop Counter Iteration with `range` ~~and `xrange`~~

#### Fixed
- Add 259 into `SUPPORTED`

### <u>0.2.4</u>  _Final_

_Release Date: 2021-08-08_

#### New

- Add support of [PEP 259](https://www.python.org/dev/peps/pep-0259) — Omit printing newline after newline

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

