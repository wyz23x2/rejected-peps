"""\
PEP INFO

PEP 326 -- A Case for Top and Bottom Values
Status: Rejected
Created: 2003-12-20

MODULE INFO

This module implements the Min (UniversalMinimum) and Max (UniversalMaximum)
singletons specified in PEP 326.

REFERENCES

PEP 326: <https://www.python.org/dev/peps/pep-0326/>
"""
PEP = 326

class _singleton(type):
    # PEP 326 says Min and Max are singletons like None
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
# The reference implementation is not used because
# 1) __cmp__ is removed
# 2) It's not a singleton in the reference implementation
class MinType(metaclass=_singleton):
    def __lt__(self, other):
        return True
    __le__ = __lt__
    def __gt__(self, other):
        return False
    def __eq__(self, other):
        # Min is only equal to itself
        return isinstance(other, type(self))
    __ge__ = __eq__
    def __repr__(self):
        return 'Min'
    __str__ = __repr__
class MaxType(metaclass=_singleton):
    def __gt__(self, other):
        return True
    __ge__ = __gt__
    def __lt__(self, other):
        return False
    def __eq__(self, other):
        # Max is only equal to itself
        return isinstance(other, type(self))
    __le__ = __eq__
    def __repr__(self):
        return 'Max'
    __str__ = __repr__
# 4 names appeared in PEP 326
Min = UniversalMinimum = MinType()
Max = UniversalMaximum = MaxType()
