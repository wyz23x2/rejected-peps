"""\
PEP INFO

PEP 313 -- Adding Roman Numeral Literals to Python
Status: Rejected
Created: 2003-04-01

MODULE INFO

This module implements the to_roman() function to convert numbers or fractions
to roman numbers, and the from_roman() function to convert roman
numbers to numbers or fractions. There are 3 modes:
- CLASSIC: Plain I, V, X etc.
- MODERN: Allow IV (4), CM (900) etc. in addition to CLASSIC
- LARGE: Allow up to 3 leading underscores before letter to mean ×1000 for each,
         for example _M -> 1000*1000 = 1000000 in addition to MODERN
The `zero` parameters control handling of zero. If None, 0 raises an error;
else it returns the value in to_roman(), and returns 0 if s is equal to it
in from_roman(). You can control the global default (first set to None) with
the default_zero attribute.

REFERENCES

PEP 313: <https://www.python.org/dev/peps/pep-0313/>
"""
PEP = 313
from numbers import Rational as _R, Integral as _I
from fractions import Fraction as _F
from functools import lru_cache as _lc
try:
    from . import pep336 as _p
except ImportError:
    try:
        import pep336 as _p
    except ImportError:
        def isNone(x):
            return x is None
    else:
        isNone = _p.isNone
        del _p
else:
    isNone = _p.isNone
    del _p

MODERN, CLASSIC, LARGE = 'modern', 'classic', 'large'
classic_dict = {1000: 'M',
                500: 'D',
                100: 'C',
                50: 'L',
                10: 'X',
                5: 'V',
                1: 'I'}
modern_dict = {1000: 'M',
               999: 'IM',
               900: 'CM',
               500: 'D',
               499: 'ID',
               400: 'CD',
               100: 'C',
               99: 'IC',
               90: 'XC',
               50: 'L',
               49: 'IL',
               40: 'XL',
               10: 'X',
               9: 'IX',
               5: 'V',
               4: 'IV',
               1: 'I'}
large_dict = {1_000_000_000_000: '___M',
              500_000_000_000: '___D',
              100_000_000_000: '___C',
              50_000_000_000: '___L',
              10_000_000_000: '___X',
              1_000_000_000: '__M',
              500_000_000: '__D',
              100_000_000: '__C',
              50_000_000: '__L',
              10_000_000: '__X',
              1_000_000: '_M',
              500_000: '_D',
              100_000: '_C',
              50_000: '_L',
              10_000: '_X'}
large_dict.update(modern_dict)
DIGITS = set(classic_dict.values())
default_zero = None

@_lc(maxsize=256, typed=True)
def _tr(x, mode, zero):
    if mode not in (MODERN, CLASSIC, LARGE):
        raise ValueError(f'Invalid mode {mode!r}')
    if isinstance(x, _R) and not isinstance(x, (_I, float)):
        # Fractions
        return f'{to_roman(x.numerator)}/{to_roman(x.denominator)}'
    try:
        x = getattr(x, '__index__', (lambda: int(x)))()
        if not isinstance(x, int):
            raise TypeError(f'Invalid __index__ type {type(x).__name__!r}')
    except Exception as e:
        try:
            x = int(x, 0)
        except Exception:
            raise e from None
    if x == 0:
        if isNone(zero):
            raise ValueError('x cannot be 0')
        return zero
    if x < 0:
        return f'-{to_roman(abs(x), mode)}'
    r = {CLASSIC: classic_dict,
         MODERN: modern_dict,
         LARGE: large_dict}[mode]
    lis = []
    for i in r:
        a, x = divmod(x, i)
        lis.append(r[i] * a)
        if x <= 0:
            break
    return ''.join(lis)
def to_roman(x: _R, mode: str = MODERN, *, zero=...) -> str:
    """Convert an int or fraction to a roman number.

    x: The number or fraction.

    mode:   There are 3 modes:
          - CLASSIC: Plain I, V, X etc.
          - MODERN: Allow IV (4), CM (900) etc. in addition to CLASSIC
          - LARGE: Allow up to 3 leading underscores before letter to mean ×1000 for each,
                   for example _M -> 1000*1000 = 1000000 in addition to MODERN

    zero: Control the handling of zero.
          If None, 0 raises an error;
          If not None, returns it when x is 0.
          You can control the global default (first set to None) with the default_zero variable.
    """
    if zero is ...:
        zero = default_zero
    return _tr(x, mode, zero)
@_lc(maxsize=256, typed=True)
def _fr(s, zero):
    if (not isNone(zero)) and s == zero:
        return 0
    if not isinstance(s, str):
        raise TypeError(f'Invalid roman string type: {type(s).__name__!r}')
    if not s:
        raise ValueError('Roman string cannot be blank')
    if s[0] == '-':
        return -from_roman(s[1:])
    if s[0] == '+':
        return +from_roman(s[1:])
    if s.count('/') == 1:
        return _F(from_roman(s.split('/')[0]),
                  from_roman(s.split('/')[1]))
    s = s.upper()
    if (set(s) - DIGITS - {'_'}) or not (set(s)-{'_'}):
        raise ValueError(f'Invalid roman numeral: {s!r}')
    result = i = 0
    for integer, num in large_dict.items():
        ln = len(num)
        while s[i:i+ln] == num:
            result += integer
            i += ln
    if result == 0:
        raise ValueError(f'Invalid roman numeral: {s!r}')
    return result
def from_roman(s: str, *, zero=...) -> _R:
    """Convert roman number (str) to an int or fraction.

    s: The roman number.

    zero: Control the handling of zero.
          If None, 0 raises an error;
          If not None, returns it when x is 0.
          You can control the global default (first set to None) with the default_zero variable.
    """
    if zero is ...:
        zero = default_zero
    return _fr(s, zero)
