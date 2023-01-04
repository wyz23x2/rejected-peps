"""\
PEP INFO

PEP 351 -- The freeze protocol
Status: Rejected
Created: 2005-04-14

MODULE INFO

This module implements the freeze() function in PEP 351. An allow_frozendict
parameter is added. If true (false by default), dicts, OrderedDicts
and defaultdicts return the manual implementation of frozendict in PEP 416
if possible.

REFERENCES

PEP 351: <https://www.python.org/dev/peps/pep-0351/>
Related:
PEP 416: <https://www.python.org/dev/peps/pep-0416/>
"""
PEP = 351

from types import MappingProxyType as _MPT
from collections.abc import Mapping as _M, Sequence as _S
def freeze(obj, *, allow_frozendict: bool = False):
    global _pep416
    try:
        hash(obj)
    except TypeError:
        # Since PEP is rejected, set, list etc. don't implement __freeze__,
        # so manual check is needed
        if isinstance(obj, set):
            return frozenset(obj)
        if isinstance(obj, _S):
            t = tuple(obj)
            return t
        if isinstance(obj, _M):
            if allow_frozendict:
                # Allow using manual PEP 416 implementation from pep416 module
                try:
                    try:
                        _pep416
                    except NameError:
                        try:
                            from . import pep416
                        except ImportError:
                            import pep416
                        _pep416 = pep416
                    d = _pep416.frozendict(obj)
                except Exception:
                    d = _MPT(obj)
            else:
                d = _MPT(obj)  # MappingProxyType by default
            return d
        # Fallback
        freezer = getattr(obj, '__freeze__', None)
        if freezer is None:
            raise TypeError(f'{type(obj).__name__!r} object is not freezable')
        return freezer()
    else:
        return obj
