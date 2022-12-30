"""\
This is where combined versions are stored.
"""
import builtins as _b
from functools import wraps as _w
def _cb(*combines):
    @_w(_cb)
    def _i(func):
        func.combines = frozenset(combines)
        return func
    return _i

# PEPs 349 & 3140
try:
    from pep3140 import _str
except ImportError:
    from . import pep3140
    _str = pep3140._str
class _str_meta(type):
    def __subclasscheck__(cls, c: type) -> bool:
        return issubclass(c, _b.str)
    def __instancecheck__(cls, i) -> bool:
        return isinstance(i, _b.str)
@_cb(349, 3140)
class str(_b.str, metaclass=_str_meta):
    def __new__(cls, arg, *args, **kwargs):
        if (not args) and (not kwargs):
            if not isinstance(arg, (_b.str, bytes)):
                arg = _str(arg)
                if not isinstance(arg, (_b.str, bytes)):
                    raise TypeError(f'__str__ returned non-string or non-{bytes.__name__} '
                                    f'(type {type(arg).__name__})')
        if isinstance(arg, _b.str) or args or kwargs:
            return _b.str.__new__(_b.str, arg, *args, **kwargs)
        else:
            return _b.bytes.__new__(_b.bytes, arg, *args, **kwargs)
    __init__ = None
