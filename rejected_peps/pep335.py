"""\
PEP INFO

PEP 335 -- Overloadable Boolean Operators
Status: Rejected
Created: 2004-08-29

MODULE INFO

This module implements the and_/AND, or_/OR & not_/NOT functions that
check for the dunder methods specified in PEP 335. NeedOtherOperand is
also implemented. These functions also have "plain" versions in the
`plain` namespace that does not do short-circuiting.

REFERENCES

PEP 335: <https://peps.python.org/pep-0335/>
"""
PEP = 335

import warnings as _w
class _singleton(type):
    # NeedOtherOperand is a singleton
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
class NeedOtherOperandType(metaclass=_singleton):
    """Returned by dunder methods when the other side is needed."""
    def __repr__(self) -> str:
        return 'NeedOtherOperand'
    __str__ = __repr__
    def __hash__(self):
        return hash(id(self))
NeedOtherOperand = NeedOtherOperandType()
_notimplemented_warning_message = ('NotImplemented should not be used '
                                   'in a boolean context. Did you mean to '
                                   'return NeedOtherOperand?')
def NOT(a) -> bool:
    """Equal to `not a`, but checks for `a.__not__()` first."""
    a_not = getattr(a, '__not__', None)
    if a_not is None:
        return not a
    a_return = a_not()
    if a_return is NeedOtherOperand or a_return is NotImplemented:
        return not a
    return bool(a_return)
not_ = NOT
class plain:
    """Namespace where versions that do not do short circuiting,
    i.e. don't call `__and1__`, exist.
    """
    def __init__(self):
        raise Exception('plain cannot be initialized')
    @staticmethod
    def AND(a, b):
        """`a and b`, but:
        - a.__and2__(b) is first checked. If a value returned, return it.
        - If a.__and2__(b) does not exist or returns NeedOtherOperand, check for b.__rand2__(a).
        - If b.__rand2__(a) does not exist or returns NeedOtherOperand, return `a and b`.
        """
        a_and = getattr(a, '__and2__', None)
        if a_and is not None:
            a_return = a_and(b)
            if a_return is NotImplemented:
                _w.warn(_notimplemented_warning_message,
                        PendingDeprecationWarning, 2)
            if a_return is not NeedOtherOperand:
                return a_return
        b_rand = getattr(b, '__rand2__', None)
        if b_rand is not None:
            b_return = b_rand(a)
            if b_return is NotImplemented:
                _w.warn(_notimplemented_warning_message,
                        PendingDeprecationWarning, 2)
            if b_return is not NeedOtherOperand:
                return b_return
        with _w.catch_warnings():
            return a and b
    and_ = AND
    @staticmethod
    def OR(a, b):
        """`a or b`, but:
        - a.__or2__(b) is first checked. If a value returned, return it.
        - If a.__or2__(b) does not exist or returns NeedOtherOperand, check for b.__ror2__(a).
        - If b.__ror2__(a) does not exist or returns NeedOtherOperand, return `a and b`.
        """
        a_or = getattr(a, '__or2__', None)
        if a_or is not None:
            a_return = a_or(b)
            if a_return is NotImplemented:
                #
                _w.warn(_notimplemented_warning_message,
                        PendingDeprecationWarning, 2)
            if a_return is not NeedOtherOperand:
                return a_return
        b_ror = getattr(b, '__ror2__', None)
        if b_ror is not None:
            b_return = b_ror(a)
            if b_return is NotImplemented:
                _w.warn(_notimplemented_warning_message,
                        PendingDeprecationWarning, 2)
            if b_return is not NeedOtherOperand:
                return a_return
        with _w.catch_warnings():
            return a or b
    or_ = OR
    NOT = not_ = staticmethod(NOT)
def AND(a, b):
    """`a and b`, but:
    - a.__and1__() is first checked. If a value returned, return it.
    - If a.__and1__() does not exist or returns NeedOtherOperand, check for a.__and2__(b).
    - If a.__and2__(b) does not exist or returns NeedOtherOperand, check for b.__rand2__(a).
    - If b.__rand2__(a) does not exist or returns NeedOtherOperand, return the classic `a and b`.
    """
    a_and = getattr(a, '__and1__', None)
    if a_and is None:
        return plain.AND(a, b)
    a_return = a_and()
    if a_return is NeedOtherOperand:
        return plain.AND(a, b)
    if a_return is NotImplemented:
        _w.warn(_notimplemented_warning_message,
                PendingDeprecationWarning, 2)
    return a_return
and_ = AND
def OR(a, b):
    """`a or b`, but:
    - a.__or__() is first checked. If a value returned, return it.
    - If a.__or1__() does not exist or returns NeedOtherOperand, check for a.__or2__(b).
    - If a.__or2__(b) does not exist or returns NeedOtherOperand, check for b.__ror2__(a).
    - If b.__ror2__(a) does not exist or returns NeedOtherOperand, return the classic `a or b`.
    """
    a_or = getattr(a, '__or1__', None)
    if a_or is None:
        return plain.OR(a, b)
    a_return = a_or()
    if a_return is NeedOtherOperand:
        return plain.OR(a, b)
    if a_return is NotImplemented:
        _w.warn(_notimplemented_warning_message,
                PendingDeprecationWarning, 2)
    return a_return
or_ = OR
