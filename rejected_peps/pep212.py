"""\
PEP INFO

PEP 212 -- Loop Counter Iteration
Status: Rejected
Created: 2000-08-22

MODULE INFO

This module implements solution #2 of PEP 212,
i.e. the indices() and irange() functions.
Note that irange() is exactly the same as PEP 279's enumerate().

REFERENCES

PEP 212: <https://peps.python.org/pep-0212/>
Related:
PEP 279: <https://peps.python.org/pep-0279/>
"""
PEP = 212
from typing import Sequence as _Seq

def indices(sequence: _Seq) -> range:
    """Return range(len(sequence))."""
    return range(len(sequence))
irange = enumerate
