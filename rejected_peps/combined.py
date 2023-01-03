"""\
This is where combined versions are stored.
"""
import builtins as _b
from functools import wraps as _w
def _cb(*combines):
    # Sets the `combines` atrribute.
    @_w(_cb)
    def _i(func):
        func.combines = frozenset(combines)
        return func
    return _i

# PEPs 349 & 3140
try:
    from pep3140 import _str
except ImportError:
    from . import pep3140 as _p
    _str = _p._str
class _str_meta(type):
    def __subclasscheck__(cls, c: type) -> bool:
        return issubclass(c, _b.str)
    def __instancecheck__(cls, i) -> bool:
        return isinstance(i, _b.str)
@_cb(349, 3140)
class str(_b.str, metaclass=_str_meta):
    """Combination of PEPs 349 & 3140.
    See pep349.str and pep3140.str for more information.
    """  # "See ..." temporary; replace it later.
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

# PEPs 204 & 281
try:
    from pep281 import range as _r
except ImportError:
    from . import pep281 as _p
    _r = _p.range
class _rliteral:
    """Combination of PEPs 204 & 281.
    Use rliteral[a:b:c] to get range(a, b, c), rliteral[:a] to get range(a).
    """
    def __getitem__(self, x) -> range:
        if isinstance(x, slice):
            start, stop, step = x.start, x.stop, x.step
            if stop is None:
                raise ValueError('Stop is required')
            if start is None:
                start = 0
            if step is None:
                step = 1
            return _r(start, stop, step)
        return _r(x)
    def __repr__(self):
        return "<class 'combined.rliteral'>"
rliteral = _cb(204, 281)(_rliteral())

# PEPs 212 & 281
try:
    from pep212 import indices
except ImportError:
    from . import pep212 as _p
    indices =  _p.indices
indices = _cb(212, 281)(indices)
