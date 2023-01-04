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

PEP 303: <https://peps.python.org/pep-0303/>
"""
PEP = 303

def divmod(dividend, *divisors) -> tuple:
    """Divide the dividend by the divisors in the order they are given.
    Returns the final quotient followed by all remainders.
    """
    # Mostly copied from PEP 303
    modulos = ()
    q = dividend
    while divisors:
        try:
            qd = q.__divmod__
        except AttributeError:
            raise TypeError(f"unsupported operand type(s) "
                            f"for divmod(): {type(q).__name__!r} and "
                            f"{type(divisors[0]).__name__!r}") from None
        qr = qd(divisors[0])
        if qr is NotImplemented:
            raise TypeError(f"unsupported operand type(s) "
                            f"for divmod(): {type(q).__name__!r} and "
                            f"{type(divisors[0]).__name__!r}")
        q, r = qr
        modulos = modulos + (r,)
        divisors = divisors[1:]
    return (q,) + modulos
def rdivmod(dividend, *divisors) -> tuple:
    """Divide the dividend by the divisors in the order reversed.
    Returns the final quotient followed by all remainders in the order given.
    """
    x = divmod(dividend, *divisors[::-1])
    return (x[0], *x[1:][::-1])
def inverse_divmod(seq, *factors):
    """The inverse operation of `divmod()`."""
    # Copied from PEP 303
    product = seq[0]
    for x, y in zip(factors, seq[1:]):
        product = product * x + y
    return product
