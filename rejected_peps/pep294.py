"""\
PEP INFO

PEP 294 -- Type Names in the types Module
Status: Rejected
Created: 2002-06-19

MODULE INFO

This module adds the lowercase regular version as in the PEP to 
the types module and this module. If the new name is invalid 
(e.g. `lambda`), a trailing underscore is added.

REFERENCES

PEP 294: <https://www.python.org/dev/peps/pep-0294/>
"""
import keyword as _k
from typing import Optional
def underscore(s: str) -> str:
    """Appends an underscore (_) to s."""
    return f'{s}_'
title = str.title
def original(s: str) -> str:
    """Returns s."""
    return s
def valid(name: str) -> bool:
    """True if name is an identifier & not a keyword. Note that non-str types return True."""
    if not isinstance(name, str):
        return True
    return _k.iskeyword(name) + (not name.isidentifier()) == 0
def apply(module=None, *, rename=underscore,
          strict: Optional[bool] = None):
    types = module or __import__('types')
    if strict is None:
        strict = rename is not original
    for name in dir(types):
        if name[-4:] == 'Type' and name[:-4]:
            new_name = name[:-4].lower()
            if not valid(new_name):
                r = rename(new_name)
                if strict and not valid(r):
                    raise ValueError(f'Invalid name {r!r}')
                new_name = r
            if strict and type(r) is not str:
                raise TypeError(f'Invalid name {new_name!r} with type '
                                f'{type(r).__name__!r}')
            setattr(types, new_name, getattr(types, name))
