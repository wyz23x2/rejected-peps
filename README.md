### What is this?

[PEPs](https://www.python.org/dev/peps/) (Python Enhancement Proposals) are a big feature of the Python programming language. Some are accepted, and some were not. This package implements some PEPs that were rejected or withdrawn.

### Which PEPs are included?

PEPs included need to match these points:

- It's not a syntax or major API change.

- It's about code, not governance etc.

- It can be implemented in pure Python code.


Parts of bytecode, C API etc. are not implemented.

### What PEPs are included now?

PEPs with a \* are slightly changed.

#### Finished

- [PEP 204](https://www.python.org/dev/peps/pep-0204/) — Range Literals
- [PEP 211](https://www.python.org/dev/peps/pep-0211/) — Adding A New Outer Product Operator
- [PEP 212](https://www.python.org/dev/peps/pep-0212/) — Loop Counter Iteration
- [PEP 265](https://www.python.org/dev/peps/pep-0265/) — Sorting Dictionaries by Value
- [PEP 276](https://www.python.org/dev/peps/pep-0276/) — Simple Iterator for `int`s
- [PEP 303](https://www.python.org/dev/peps/pep-0303/) — Extend `divmod()` for Multiple Divisors
- [PEP 326](https://www.python.org/dev/peps/pep-0326/) — A Case for Top and Bottom Values
- [PEP 336](https://www.python.org/dev/peps/pep-0336/) — Make `None` callable
- [PEP 349](https://www.python.org/dev/peps/pep-0349/)\* – Allow `str()` to return ~~unicode strings~~ bytes
- [PEP 351](https://www.python.org/dev/peps/pep-0351/) — The `freeze` protocol
- [PEP 416](https://www.python.org/dev/peps/pep-0416/) — Add a `frozendict` builtin type
- [PEP 559](https://www.python.org/dev/peps/pep-0559/) — Built-in `noop()`
- [PEP 3140](https://www.python.org/dev/peps/pep-3140/) – `str(container)` should call `str(item)`, not `repr(item)`

#### Developing

- [PEP 313](https://www.python.org/dev/peps/pep-0313/)\* – Adding Roman Numeral ~~Literals~~ Functions to Python
- [PEP 335](https://www.python.org/dev/peps/pep-0335/)\* – Overloadable Boolean ~~Operators~~ Operator Functions

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
pepinfo(number=416, title='Add a frozendict builtin type', status='Rejected', creation='2012-02-29', url='https://www.python.org/dev/peps/pep-0416/')
>>> rp.SUPPORTED
frozenset({416, 3140, 326, 265, 303, 336, 559, 211, 212, 276, 349, 351})
>>> 
```

