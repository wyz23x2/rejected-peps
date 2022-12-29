import sys
try:
    from . import pep211 as _p
except ImportError:
    try:
        import pep211 as _p
    except ImportError as e:
        _imp_e = e
        _imp_e.__suppress_context__ = True
        _p = None
class pep204:
    """\
PEP INFO

PEP 204 -- Range Literals
Status: Rejected
Created: 2000-07-14

MODULE INFO

This module supports indexing for range literals:
>>> import rejected_peps.pep204 as r
>>> r[5]
range(0, 5)
>>> r[2:5]
range(2, 5)
>>> r[60:40:-2]
range(60, 40, -2)

REFERENCES

PEP 204: <https://www.python.org/dev/peps/pep-204/>
"""
    PEP = 204
    def __getitem__(self, x) -> range:
        if isinstance(x, slice):
            start, stop, step = x.start, x.stop, x.step
            if stop is None:
                raise ValueError('Stop is required')
            if start is None:
                start = 0
            if step is None:
                step = 1
            return range(start, stop, step)
        return range(x)
    def __repr__(self) -> str:
        if _p is None:
            raise ValueError('repr unavailable') from _imp_e
        return repr(_p).replace('pep211', 'pep204')
sys.modules[__name__] = pep204()
