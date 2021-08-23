"""\
PEP INFO

PEP 754 -- IEEE 754 Floating Point Special Values
Status: Rejected
Created: 2003-03-28

MODULE INFO

This module implements NaN, PosInf, NegInf and the functions
in PEP 754.

REFERENCES

PEP 754: <https://www.python.org/dev/peps/pep-0754/>
"""
PEP = 754
import math as _math

NaN = float('nan')
PosInf = float('inf')
NegInf = -PosInf
def isNaN(value) -> bool:
    return _math.isnan(value)
def isPosInf(value) -> bool:
    return _math.isinf(value) and value > 0
def isNegInf(value) -> bool:
    return _math.isinf(value) and value < 0
def isFinite(value) -> bool:
    return _math.isfinite(value)
def isInf(value) -> bool:
    return _math.isinf(value)
