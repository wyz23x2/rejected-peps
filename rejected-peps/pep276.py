"""\
PEP INFO

PEP 276 -- Simple Iterator for ints
Status: Rejected
Created: 2001-11-12

MODULE INFO

This module implements the iterable IntType in PEP 276.

REFERENCES

PEP 276: <https://www.python.org/dev/peps/pep-0276/>
"""
PEP = 276

class IntType(int):
    def __iter__(self):
        if self < 0:
            return iter(())
        return iter(range(__builtins__.int(self)))
int = IntType
