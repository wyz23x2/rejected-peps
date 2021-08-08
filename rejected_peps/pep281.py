"""\
PEP INFO

PEP 281 -- Loop Counter Iteration with range and xrange
Status: Rejected
Created: 2002-02-11

MODULE INFO

This module changes range into a function that runs like specified in PEP 281.

REFERENCES

PEP 281: <https://www.python.org/dev/peps/pep-0281/>
"""
PEP = 281

def range(*args):
    a = []
    for arg in args:
        try:
            a.append(arg.__index__())
        except (AttributeError, ValueError):
            try:
                a.append(len(arg))
            except (TypeError, ValueError):
                raise TypeError(f'TypeError: {type(arg).__name__!r} object '
                                'cannot be interpreted '
                                'as an integer') from None
    return range(*a)
