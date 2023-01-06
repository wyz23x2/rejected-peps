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
from reprlib import recursive_repr as _rr
from collections.abc import Container as _C, Mapping as _M

@_rr()
def _str(x) -> _b.str:
    if (not isinstance(x, _C)) or isinstance(x, (_b.str, bytes)):
        xs = getattr(x, '__str__', None)
        if xs is not None:
            try:
                value = xs()
                if value is not NotImplemented:
                    return value
            except TypeError:
                xs = getattr(x.__class__, '__str__', None)
                if xs is not None:
                    try:
                        value = xs(x)
                        if value is not NotImplemented:
                            return value
                    except TypeError:
                        pass
        return x.__repr__()
    if isinstance(x, (dict, _M)):
        if type(x) is dict:  # no subclasses
            # {}
            prefix = suffix = ''
        else:
            # X({})
            ss = _b.str(x)
            try:
                si, ei = ss.index('{'), len(ss)-1-ss[::-1].index('}')
            except ValueError:
                prefix, suffix = f'{type(x).__name__}(', ')'
            else:
                prefix, suffix = ss[:si], ss[ei+1:]
        if not x:  # Empty
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
class _str_meta(type):
    def __subclasscheck__(cls, c: type) -> bool:
        return issubclass(c, _b.str)
    def __instancecheck__(cls, i) -> bool:
        return isinstance(i, _b.str)
class str(_b.str, metaclass=_str_meta):
    def __new__(cls, arg, *args, **kwargs):
        if (not args) and (not kwargs):
            arg = _str(arg)
        return _b.str.__new__(_b.str, arg, *args, **kwargs)
    __init__ = None
