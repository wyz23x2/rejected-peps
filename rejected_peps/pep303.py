"""\
PEP INFO

PEP 303 -- Extend divmod() for Multiple Divisors
Status: Rejected
Created: 2002-12-31

MODULE INFO

This module changes divmod() mostly following the PEP. However, divmod()
divides the divisors with the first divisor first. Last divisor first
like proposed is the rdivmod() function. The inverse_divmod function
from PEP 303 is also added.

REFERENCES

PEP 303: <https://www.python.org/dev/peps/pep-0303/>
"""
PEP = 303

def divmod(dividend, *divisors) -> tuple:
    # Mostly copied from PEP 303
    modulos = ()
    q = dividend
    while divisors:
        try:
            qd = q.__divmod__
        except AttributeError:
            raise ValueError(f"TypeError: unsupported operand type(s) "
                             f"for divmod(): {type(q).__name__!r} and "
                             f"{type(divisors[0]).__name__!r}") from None
        qr = qd(divisors[0])
        if qr is NotImplemented:
            raise ValueError(f"TypeError: unsupported operand type(s) "
                             f"for divmod(): {type(q).__name__!r} and "
                             f"{type(divisors[0]).__name__!r}")
        q, r = qr
        modulos = (r,) + modulos
        divisors = divisors[1:]
    return (q,) + modulos
def rdivmod(dividend, *divisors) -> tuple:
    return divmod(dividend, *divisors[::-1])
def inverse_divmod(seq, *factors):
    # Copied from PEP 303
    product = seq[0]
    for x, y in zip(factors, seq[1:]):
        product = product * x + y
    return product
