"""\
PEP INFO

PEP 416 -- Add a frozendict builtin type
Status: Rejected
Created: 2012-02-29

MODULE INFO

This module implements the frozendict type described in PEP 416. Note that since dict
is ordered in supported versions, frozendict is also ordered.

REFERENCES

PEP 416: <https://www.python.org/dev/peps/pep-0416/>
Related:
PEP 351: <https://www.python.org/dev/peps/pep-0351/>
"""
PEP = 416

# Cannot subclass types.MappingProxyType
class frozendict(dict):
    # Mostly copied from PEP 351 "Sample implementations"
    def __hash__(self) -> int:
        # PEP 416:
        # > However, frozendict values can be not hashable.
        # > A frozendict is hashable if and only if all values are hashable.
        hashes = [], []
        # Needs two to avoid mixing keys and values, e.g.
        # hash(frozendict({1: 2, 3: 4})) and hash(frozendict({1: 3, 2: 4}))
        for k, v in self.items():
            hashes[0].append(hash(k))
            hashes[1].append(hash(v))
        # PEP 416:
        # > · frozendict hash does not depend on the items creation order
        hashes[0].sort()
        hashes[1].sort()
        return hash((tuple(hashes[0]), tuple(hashes[1])))
    def __repr__(self) -> str:
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
