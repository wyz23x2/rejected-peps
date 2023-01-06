"""\
PEP INFO

PEP 559 -- Built-in noop()
Status: Rejected
Created: 2017-09-08

MODULE INFO

This module implements the noop() function in PEP 559 that takes
any arguments and directly returns None.

REFERENCES

PEP 559: <https://peps.python.org/pep-0559/>
"""
PEP = 559

def noop(*args, **kws) -> None:
    """Do nothing and return None."""
    # Copied
    return None
