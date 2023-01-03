"""\
PEP INFO

PEP 281 -- Loop Counter Iteration with range and xrange
Status: Rejected
Created: 2002-02-11

MODULE INFO

This module changes range into a function that runs like specified in PEP 281.

REFERENCES

PEP 281: <https://www.python.org/dev/peps/pep-0281/>
"""
PEP = 281
import builtins as _b

class _range_meta(type):
    def __subclasscheck__(cls, c: type) -> bool:
        return issubclass(c, _b.range)
    def __instancecheck__(cls, i) -> bool:
        return isinstance(i, _b.range)
    def __getattr__(cls, attr: str):
        return getattr(_b.range, attr)
    def __and__(cls: type, cls1) -> type:
        try:
            from . import pep212, pep204
        except ImportError:
            import pep212, pep204
        if cls1 == pep204:
            return NotImplemented
        if cls1 != pep212.indices:
            raise TypeError(f'Cannot combine {cls!r} and {cls1!r}')
        return cls1
    __rand__ = __and__
class range(metaclass=_range_meta):
    """Same as `builtins.range`, but sequence arguments are converted to their lengths."""
    def __new__(cls, *args):
        a = []
        for arg in args:
            try:
                a.append(arg.__index__())
            except (AttributeError, ValueError):
                try:
                    a.append(len(arg))
                except (TypeError, ValueError):
                    raise TypeError(f'TypeError: {type(arg).__name__!r} object '
                                    'cannot be interpreted '
                                    'as an integer or sequence') from None
        return _b.range.__new__(_b.range, *a)
    __init__ = None
