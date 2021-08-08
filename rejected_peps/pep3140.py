"""\
PEP INFO

PEP 3140 -- str(container) should call str(item), not repr(item)
Status: Rejected
Created: 2008-05-27

MODULE INFO

This module changes str() to a function matching behavior 
described in the PEP.

REFERENCES

PEP 3140: <https://www.python.org/dev/peps/pep-3140/>
"""
PEP = 3140
import builtins as _b
from collections.abc import Container as _C, Mapping as _M

def str(x, *args, **kwargs):
    if args or kwargs:
        return _b.str(x, *args, **kwargs)
    if (not isinstance(x, _C)) or isinstance(x, (_b.str, bytes)):
        xs = getattr(x, '__str__', None)
        if xs is not None:
            value = xs()
            if value is not NotImplemented:
                return value
        return x.__repr__()
    if isinstance(x, (dict, _M)):
        if isinstance(x, dict):
            prefix = suffix = ''
        else:
            prefix, suffix = f'{type(x).__name__}(', ')'
        if not x:
            return '%s{}%s' % (prefix, suffix)
        parts = [prefix, '{']
        for key, value in x.items():
            parts.extend((f'{key!s}: {value!s}', ', '))
        parts = [*parts[:-1], '}', suffix]
        return ''.join(parts)
    else:
        cls = type(x)
        prefix, suffix = {list: ('[', ']'),
                          tuple: ('(', ')'),
                          set: ('{', '}'),
                          }.get(cls, (f'{cls.__name__}([', '])'))
        parts = [prefix]
        for item in x:
            parts.extend((str(item), ', '))
        if not (isinstance(x, tuple) and len(x) == 1):
            if len(x):
                parts = parts[:-1]
        else:
            parts[-1] = ','
        return ''.join((*parts, suffix))
