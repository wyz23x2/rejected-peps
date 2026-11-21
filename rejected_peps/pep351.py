"""\
PEP INFO

PEP 351 -- The freeze protocol
Status: Rejected
Created: 2005-04-14

MODULE INFO

This module implements the freeze() function in PEP 351.

REFERENCES

PEP 351: <https://peps.python.org/pep-0351/>
Related:
PEP 416: <https://peps.python.org/pep-0416/>
PEP 814: <https://peps.python.org/pep-0814/>
"""
PEP = 351

from typing import Literal as _L, overload as _ov, Any as _A
from warnings import deprecated as _deprecated, warn as _warn, catch_warnings as _cw
from types import MappingProxyType as _MPT
from collections.abc import Mapping as _M, Sequence as _S, Callable as _C

@_ov
def freeze(obj, /, *,
           frozendict_type: _L[416]|_C[[dict], _A]|bool = False):
    ...
@_ov
@_deprecated('allow_frozendict is deprecated and will be removed in v1.0. Specify `frozendict_type` instead.')
def freeze(obj, /, *, allow_frozendict: bool = False):
    ...
def freeze(obj, /, *,
           allow_frozendict: bool|None = None,  # Deprecated
           frozendict_type: _L[416]|_C[[dict], _A]|bool = False):
    """frozendict_type: 416 for pep416.frozendict; True for builtins.frozendict, False for MappingProxyType (default); or any other callable."""
    # Temporary docstring for migration; formal ones are to be added in v1.0
    global _pep416
    if allow_frozendict is not None:
        if frozendict_type is not False:
            raise ValueError('Only frozendict_type shall be passed')
        _warn('allow_frozendict is deprecated and will be removed in v1.0. Specify frozendict_type instead.',
             DeprecationWarning, stacklevel=2)
    elif not (frozendict_type is True or
              frozendict_type is False or
              callable(frozendict_type) or
              (isinstance(frozendict_type, int) and frozendict_type == 416)):
        raise TypeError('frozendict_type must be None, a callable or 416 (int)')
    try:
        hash(obj)
    except TypeError:
        # Code moved outside to avoid 'unhashable type' error appearing
        pass
    else:
        return obj
    # Since PEP is rejected, set, list etc. don't implement __freeze__,
    # so manual check is needed
    if isinstance(obj, set):
        return frozenset(obj)
    if isinstance(obj, _S):
        t = tuple(obj)
        return t
    if isinstance(obj, _M):
        with _cw(category=ImportWarning, action='ignore'):
            if allow_frozendict:
                # Allow using manual PEP 416 implementation from pep416 module (or builtin)
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
            elif allow_frozendict is False:
                d = _MPT(obj)
            elif frozendict_type == 416:
                try:
                    _pep416
                except NameError:
                    try:
                        from . import pep416
                    except ImportError:
                        import pep416
                    _pep416 = pep416
                d = _pep416.frozendict(obj)
            elif frozendict_type is True:
                from builtins import frozendict  # type: ignore
                d = frozendict(obj)
            elif frozendict_type is False:
                d = _MPT(obj)
            else:
                d = frozendict_type(obj)
        return d
    # Fallback
    freezer = getattr(obj, '__freeze__', None)
    if freezer is None:
        raise TypeError(f'{type(obj).__name__!r} object is not freezable')
    return freezer()
