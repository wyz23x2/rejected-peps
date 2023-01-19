"""\
PEP INFO

PEP 294 -- Type Names in the types Module
Status: Rejected
Created: 2002-06-19

MODULE INFO

The apply(module=types, *, rename=underscore, strict=bool) function
adds the lowercase regular version as in the PEP to
the module. If the new name is invalid (e.g. `lambda`), rename(name)
is called. If strict is True, then the new return value of rename()
and the type (should be str) will be checked. This is done in-place
so apply() returns None.
The underscore(), title() and original() functions are provided
for the rename parameter.
See the docstrings for more information.

REFERENCES

PEP 294: <https://peps.python.org/pep-0294/>
"""
PEP = 294
import keyword as _k
import threading as _t
from importlib import import_module as _im
from typing import Optional as _O, Callable as _C

def underscore(s: str) -> str:
    """Appends an underscore (_) to s."""
    if not isinstance(s, str):
        raise TypeError(f's must be str, not {type(s).__name__}')
    return f'{s}_'
title = str.title
def original(s: str) -> str:
    """Returns s."""
    if not isinstance(s, str):
        raise TypeError(f's must be str, not {type(s).__name__}')
    return s
def valid(name) -> bool:
    """True if name is an identifier & not a keyword. Note that non-str types return True."""
    if not isinstance(name, str):
        return True
    return _k.iskeyword(name) + (not name.isidentifier()) == 0

_apply_lock = _t.RLock()
def apply(module=None, *, mapfunc: _O[_C] = None, rename: _O[_C] = None,
          strict: _O[bool] = None):
    """Add the lowercase regular version as in PEP 294 to
    the module after processed by `mapfunc` (default `original`).
    If the new name is invalid (e.g. `lambda`), `rename(name)`
    is called.
    If strict is True, then the new return value of `rename(name)`
    and the type (should be str) will be checked. If `None`, true only if `rename` is `original`.
    Returns the modified module.
    """
    mapfunc = mapfunc or original
    rename = rename or underscore
    if strict is None:
        strict = rename is not original
    with _apply_lock:
        types = module or _im('types')
        for name in dir(types):
            new_name = mapfunc(name[:-4].lower())
            if name[-4:] == 'Type' and name[:-4]:
                if not valid(new_name):
                    r = rename(new_name)
                    if strict and not valid(r):
                        raise ValueError(f'Invalid name {r!r}')
                    new_name = r
                if strict and type(new_name) is not str:
                    # str subclasses aren't allowed
                    raise TypeError(f'Invalid name {new_name!r} with type '
                                    f'{type(r).__name__!r}')
                setattr(types, new_name, getattr(types, name))
        return types
