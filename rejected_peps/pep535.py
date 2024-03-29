"""\
PEP INFO

PEP 535 -- Rich comparison chaining
Status: Deferred
Created: 2016-11-12

MODULE INFO

This module adds cmp(obj, op, obj, ..., andfunc=None) that implements rich comparison chaining.
If andfunc is not None, andfunc is used instead of and, else obj.__andfunc__ is checked;
then it falls back onto and.

REFERENCES

PEP 535: <https://www.python.org/dev/peps/pep-0535/>
"""
PEP = 535
from typing import Callable as _C, Optional as _O

# Constants
LT = '<'
LE = '<='
EQ = '=='
NE = '!='
GE = '>='
GT = '>'
VALID = frozenset((LT, LE, EQ, NE, GE, GT))

# Functions
def _cmp(a, op: str, b):
    # Use match/case in 3.10+
    if not isinstance(op, str):
        raise TypeError(f'Invalid op {op!r}')
    if op == '<': return a < b
    if op == '<=': return a <= b
    if op == '==': return a == b
    if op == '!=': return a != b
    if op == '>=': return a >= b
    if op == '>': return a > b
    raise ValueError(f'Invalid op {op!r}')
def cmp(*args, and_func: _O[_C] = None):
    if len(args) % 2 == 0:
        raise ValueError(f'Invalid arguments ({len(args)}; should be odd)')
    obj = args[::2]
    op = args[1::2]
    b = _cmp(obj[0], op[0], obj[1])
    for i in range(1, len(obj)-1):
        c = _cmp(obj[i], op[i], obj[i+1])
        if and_func is None:
            if hasattr(b, '__andfunc__'):
                b = b.__andfunc__(c)
            elif hasattr(c, '__randfunc__'):
                b = c.__randfunc__(b)
            else:
                try:
                    b = b and c
                except Exception as e:
                    try:
                        e.add_note('Error occurred while falling back to '
                                   '{b!r} and {c!r}')
                    except AttributeError:
                        raise e
                    else:
                        raise e from None
        else:
            b = and_func(b, c)
    return b
