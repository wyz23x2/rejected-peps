"""\
PEP INFO

PEP 349 -- Allow str() to return unicode strings
Status: Rejected
Created: 2005-08-02

MODULE INFO

This module changes str() to allow returning **bytes**.
Since all strings are unicode starting from Python 3,
the title is changed. Note that three argument form is
still implemented as normal.

REFERENCES

PEP 349: <https://peps.python.org/pep-0349/>
"""
PEP = 349
import builtins as _b

bytes = _b.bytes
class _str_meta(type):
    def __subclasscheck__(cls, c: type) -> bool:
        return issubclass(c, _b.str)
    def __instancecheck__(cls, i) -> bool:
        return isinstance(i, _b.str)
    def __and__(cls: type, cls2: type) -> type:
        try:
            from . import pep3140
        except ImportError:
            import pep3140
        if cls2 == pep3140.str:
            try:
                from . import combined
            except ImportError:
                import combined
            return combined.str
        raise TypeError(f'Cannot combine {cls!r} and {cls2!r}')
    __rand__ = __and__
class str(_b.str, metaclass=_str_meta):
    """Same as `builtins.str`, but a `bytes` is returned if `__str__` returns bytes.
    The str(bytes_or_buffer, encoding[, errors]) form is unchanged.
    """
    def __new__(cls, arg, *args, **kwargs):
        if (not args) and (not kwargs):
            if not isinstance(arg, (_b.str, bytes)):
                arg = arg.__str__()
                if not isinstance(arg, (_b.str, bytes)):
                    raise TypeError(f'__str__ returned non-string or non-{bytes.__name__} '
                                    f'(type {type(arg).__name__})')
        if isinstance(arg, _b.str) or args or kwargs:
            return _b.str.__new__(_b.str, arg, *args, **kwargs)
        else:
            return _b.bytes.__new__(_b.bytes, arg, *args, **kwargs)
    __init__ = None
