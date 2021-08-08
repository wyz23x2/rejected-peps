"""\
PEP INFO

PEP 349 -- Allow str() to return unicode strings
Status: Rejected
Created: 2005-08-02

MODULE INFO

This module changes str() to allow returning **bytes**. 
Since all strings are unicode starting from Python 3, 
the title is changed. Note that str() is made a function, 
and the three argument form is disallowed.

REFERENCES

PEP 349: <https://www.python.org/dev/peps/pep-0349/>
"""
PEP = 349
import builtins as _b
# NOTE: bytearrays may be supported too, but not do it yet. <2021-08-08>

def str(object=''):
    if isinstance(object, (_b.str, bytes)):
        return object
    r = object.__str__()
    if not isinstance(r, (_b.str, bytes)):
        raise TypeError('__str__ returned non-string or non-bytes')
    return r
