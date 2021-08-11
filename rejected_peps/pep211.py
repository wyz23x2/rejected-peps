"""\
PEP INFO

PEP 211 -- Adding A New Outer Product Operator
Status: Rejected
Created: 2000-07-15

MODULE INFO

This module implements a wrapper that enables the @ operator 
to mean itertools.product. Call the wrapper to get the original object.

REFERENCES

PEP 211: <https://www.python.org/dev/peps/pep-0211/>
"""
PEP = 211

from itertools import product
class wrapper:
    def __init__(self, obj):
        self._obj = obj
    def __matmul__(self, other) -> product:
        return product(self(), getattr(other, '_obj', other))
    def __rmatmul__(self, other) -> product:
        return product(getattr(other, '_obj', other), self())
    def __call__(self):
        return self._obj
