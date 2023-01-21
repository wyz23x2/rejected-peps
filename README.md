[![Version](https://img.shields.io/static/v1?label=develop&message=v1.0.0dev1&color=important&logo=semver)](
https://pypi.org/project/rejected-peps/1.0.0.dev1/)
[![Python: >=3.7](https://img.shields.io/static/v1?label=Python&message=3.7%21%20%28~Jan%2027%29%20|%20>%3D3.8&color=informational&logo=python&logoColor=gold)](
https://github.com/wyz23x2/rejected-peps/)
[![Lines](https://img.shields.io/tokei/lines/github/wyz23x2/rejected-peps?logoColor=blue&logo=code%20review&label=Total%20lines)](https://github.com/wyz23x2/rejected-peps/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/rejected-peps.svg?logo=pypi&logoColor=skyblue&label=PyPI%20downloads)](
https://pypi.org/project/rejected-peps/)
[![License: MIT](https://img.shields.io/pypi/l/rejected-peps.svg?color=success&label=License)](
https://pypi.org/project/rejected-peps/)
[![Security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
<!-- [![Python versions: >=3.7](https://img.shields.io/pypi/pyversions/rejected-peps.svg?logo=python&logoColor=gold&label=Python)](
https://pypi.org/project/rejected-peps/) -->
### What is this?

[PEPs](https://peps.python.org/) (Python Enhancement Proposals) are a special part of the Python programming language. Some were accepted, and some were not. This package implements some PEPs that were rejected, deferred or withdrawn.

### What PEPs are included?

A PEP included needs to match these points:

- It's not a syntax or major API change, or has a simple and clear way to bypass it.

- It's about code, not governance etc.

- It can be implemented in pure Python code.


Parts related to the bytecode, C API etc. are not implemented.

### Which PEPs are included now?

PEPs with an \* are slightly modified.

#### Finished (20)

- [PEP 204](https://peps.python.org/pep-0204/) — Range Literals
- [PEP 211](https://peps.python.org/pep-0211/) — Adding A New Outer Product Operator
- [PEP 212](https://peps.python.org/pep-0212/) — Loop Counter Iteration
- [PEP 259](https://peps.python.org/pep-0259/) — Omit printing newline after newline
- [PEP 265](https://peps.python.org/pep-0265/) — Sorting Dictionaries by Value
- [PEP 276](https://peps.python.org/pep-0276/) — Simple Iterator for `int`s
- [PEP 281](https://peps.python.org/pep-0281/)\* – Loop Counter Iteration with `range` ~~and `xrange`~~
- [PEP 294](https://peps.python.org/pep-0294/) — Type Names in the types Module
- [PEP 303](https://peps.python.org/pep-0303/) — Extend `divmod()` for Multiple Divisors
- [PEP 313](https://peps.python.org/pep-0313/)\* – Adding Roman Numeral ~~Literals~~ Functions to Python
- [PEP 326](https://peps.python.org/pep-0326/) — A Case for Top and Bottom Values
- [PEP 335](https://peps.python.org/pep-0335/)\* – Overloadable Boolean ~~Operators~~ Operator Functions
- [PEP 336](https://peps.python.org/pep-0336/) — Make `None` callable
- [PEP 349](https://peps.python.org/pep-0349/)\* – Allow `str()` to return ~~unicode strings~~ bytes
- [PEP 351](https://peps.python.org/pep-0351/) — The `freeze` protocol
- [PEP 416](https://peps.python.org/pep-0416/) — Add a `frozendict` builtin type
- [PEP 535](https://peps.python.org/pep-0535/) — Rich comparison chaining
- [PEP 559](https://peps.python.org/pep-0559/) — Built-in `noop()`
- [PEP 754](https://peps.python.org/pep-0754/) — IEEE 754 Floating Point Special Values
- [PEP 3140](https://peps.python.org/pep-3140/) – `str(container)` should call `str(item)`, not `repr(item)`

<!--#### Developing (1)

- [PEP 601](https://peps.python.org/pep-0601/) — Forbid `return`/`break`/`continue` breaking out of `finally`-->

### How do I use it?
Wiki is coming soon!

Quick example:

```python
>>> import rejected_peps as rp
>>> rp.pep(559).noop()   # Function call
>>> Min = rp.pep326.Min  # Module
>>> Min < 3.14
True
>>> Min == -10, Min == Min
(False, True)
>>> rp.info(416)
pepinfo(number=416, title='Add a frozendict builtin type', status='Rejected', creation='2012-02-29', url='https://peps.python.org/pep-0416/')
>>> rp.SUPPORTED
frozenset({259, 265, ..., 351, 754})
>>> 
```
