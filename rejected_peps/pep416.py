"""\
PEP INFO

PEP 416 -- Add a frozendict builtin type
Status: Rejected
Created: 2012-02-29

MODULE INFO

This module implements the frozendict type described in PEP 416. Note that
since dict is ordered in supported versions, frozendict is also ordered.

REFERENCES

PEP 416: <https://peps.python.org/pep-0416/>
Related:
PEP 351: <https://peps.python.org/pep-0351/>

Note for Python >=3.15: PEP 814 is accepted replacing this implementation.
PEP 814: <https://peps.python.org/pep-0814/>
"""
PEP = 416
__all__ = ['frozendict']

from sys import version_info
# from warnings import warn

# Cannot subclass types.MappingProxyType
# Note: builtins.frozendict in 3.15 is *not* a subclass of dict.
class frozendict(dict):
    # Mostly copied from PEP 351 "Sample implementations"
    def __hash__(self, /) -> int:
        # PEP 416:
        # > However, frozendict values can be not hashable.
        # > A frozendict is hashable if and only if all values are hashable.
        # > · frozendict hash does not depend on the items creation order
        # Implementation borrowed from PEP 814 (v0.9.10)
        return hash(frozenset(self.items()))
    def __repr__(self, /) -> str:
        return f'{type(self).__name__}({super().__repr__()})'
    def __immutable(self, *args, **kwargs):
        raise TypeError(f'{type(self).__name__!r} object is immutable')
    __setitem__ = __immutable
    __delitem__ = __immutable
    clear       = __immutable
    update      = __immutable
    setdefault  = __immutable
    pop         = __immutable
    popitem     = __immutable
    def __dir__(self, /):
        return (set(object.__dir__(self))
                -{'__setitem__', '__delitem__',
                  'clear', 'update', 'setdefault', 'pop',
                  'popitem', f'_{type(self).__name__}__immutable'})
