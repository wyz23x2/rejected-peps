"""\
PEP INFO

PEP 276 -- Simple Iterator for ints
Status: Rejected
Created: 2001-11-12

MODULE INFO

This module implements the iterable IntType in PEP 276.

REFERENCES

PEP 276: <https://peps.python.org/pep-0276/>
"""
PEP = 276
import builtins as _b

class IntType(_b.int):
    """Same as `builtins.int`, but `iter(x)` returns `range(max(x, 0))`."""
    def __iter__(self):
        if self < 0:
            return iter(())
        return iter(range(_b.int(self)))
int = IntType
