"""\
PEP INFO

PEP 313 -- Adding Roman Numeral Literals to Python
Status: Rejected
Created: 2003-04-01

MODULE INFO

This module implements the roman() function to convert numbers 
to roman numbers, and the to_int() function to convert roman 
numbers to ints. There are 3 modes:
- CLASSIC: Plain I, V, X etc.
- MODERN: Allow IV (4), CM (900) etc. in addition to CLASSIC
- LARGE: Allow up to 2 leading underscores before letter to mean ×1000,
         for example _M -> 1000*1000 = 1000000 in addition to MODERN
The zero parameters control handling of zero. If None, 0 raises an error; 
else it returns the value in roman(), and returns 0 if s is equal to it 
in to_int(). You can control the global default (first set to None) with 
the zero attribute.

REFERENCES

PEP 313: <https://www.python.org/dev/peps/pep-0313/>
"""
from numbers import Rational as _R, Integral as _I
MODERN, CLASSIC, LARGE = 'modern', 'classic', 'large'
classic_dict = {1000: 'M',
                500: 'D',
                100: 'C',
                50: 'L',
                10: 'X',
                5: 'V',
                1: 'I'}
modern_dict = {1000: 'M',
               900: 'CM',
               500: 'D',
               400: 'CD',
               100: 'C',
               90: 'XC',
               50: 'L',
               40: 'XL',
               10: 'X',
               9: 'IX',
               5: 'V',
               4: 'IV',
               1: 'I'}
large_dict = {1_000_000_000: '__M',
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
zero = None
def roman(x, mode=MODERN, *, zero=zero):
    if mode not in (MODERN, CLASSIC, LARGE):
        raise ValueError(f'Invalid mode {mode!r}')
    if isinstance(x, _R) and not isinstance(x, (_I, float)):
        return f'{roman(x.numerator)}/{roman(x.denominator)}'
    try:
        x = int(x)
    except Exception as e:
        try:
            x = int(x, 0)
        except Exception:
            raise e from None
    if x == 0:
        if zero is None:
            raise ValueError('x cannot be 0')
        return zero
    if x < 0:
        return f'-{roman(abs(x))}'
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
def to_int(s, *, zero=zero):
    if zero is not None and s == zero:
        return 0
    if not isinstance(s, str):
        raise TypeError(f'Invalid roman string type: {type(s).__name__!r}')
    if not s:
        raise ValueError('Roman string cannot be blank')
    if s[0] == '-':
        return -to_int(s[1:])
    if s[0] == '+':
        return +to_int(s[1:])
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