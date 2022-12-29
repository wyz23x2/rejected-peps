"""\
PEP INFO

PEP 535 -- Rich comparison chaining
Status: Deferred
Created: 2016-11-12

MODULE INFO

This module adds NoneType that makes None callable,
and instance none (None is a keyword). This breaks the `x is None` usage,
so `isNone(obj)` checks if obj is None or none.

REFERENCES

PEP 535: <https://www.python.org/dev/peps/pep-0535/>
"""
PEP = 535
