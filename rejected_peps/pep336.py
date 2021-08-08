"""\
PEP INFO

PEP 336 -- Make None callable
Status: Rejected
Created: 2004-10-28

MODULE INFO

This module adds NoneType that makes None callable, 
and instance none (None is a keyword). This breaks the `x is None` usage, 
so `isNone(obj)` checks if obj is None or none.

REFERENCES

PEP 336: <https://www.python.org/dev/peps/pep-0336/>
"""
PEP = 336

class _singleton(type):
    # None is a singleton
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
class NoneType(metaclass=_singleton):
    def __repr__(self):
        return 'None'
    __str__ = __repr__
    def __call__(self, *args, **kwargs):
        return self
    def __eq__(self, other):
        return isinstance(other, type(self)) or other is None
none = NoneType()
def isNone(object):
    return object is NoneType() or object is None
