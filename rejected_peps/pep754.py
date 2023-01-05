"""\
PEP INFO

PEP 754 -- IEEE 754 Floating Point Special Values
Status: Rejected
Created: 2003-03-28

MODULE INFO

This module implements NaN, PosInf, NegInf and the functions
in PEP 754.

REFERENCES

PEP 754: <https://peps.python.org/pep-0754/>
"""
PEP = 754
import math as _math

NaN = float('nan')
PosInf = float('inf')
NegInf = -PosInf
def isNaN(value) -> bool:
    """Return True if x is a NaN (not a number), and False otherwise."""
    return _math.isnan(value)
def isPosInf(value) -> bool:
    """Return True if x is a positive infinity, and False otherwise."""
    return _math.isinf(value) and value > 0
def isNegInf(value) -> bool:
    """Return True if x is a negative infinity, and False otherwise."""
    return _math.isinf(value) and value < 0
def isFinite(value) -> bool:
    """Return True if x is neither an infinity nor a NaN, and False otherwise."""
    return _math.isfinite(value)
def isInf(value) -> bool:
    """Return True if x is a positive or negative infinity, and False otherwise."""
    return _math.isinf(value)
