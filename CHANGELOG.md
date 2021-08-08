# Rejected-PEPs Changelog

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

