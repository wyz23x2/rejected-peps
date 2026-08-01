"""\
PEP INFO

PEP 211 -- Adding A New Outer Product Operator
Status: Rejected
Created: 2000-07-15

MODULE INFO

This module implements a wrapper that enables the @ operator
to mean itertools.product. Call the wrapper to get the original object.

REFERENCES

PEP 211: <https://peps.python.org/pep-0211/>
"""
PEP = 211

from itertools import product
class wrapper:
    def __init__(self, obj, /):
        self._obj = obj
    def __repr__(self):
        return f'{self.__class__.__name__}({self._obj!r})'
    def __matmul__(self, other) -> product:
        try:
            return product(self(), getattr(other, '_obj', other))
        except TypeError:
            try:
                return product(self(), repeat=other)
            except TypeError:
                return NotImplemented
    def __rmatmul__(self, other) -> product:
        try:
            return product(getattr(other, '_obj', other), self())
        except TypeError:
            return NotImplemented
    def __call__(self):
        return self._obj
    @property
    def __wrapped__(self):
        return self._obj
