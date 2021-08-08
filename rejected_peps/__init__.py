__version__ = '0.1.1'
import importlib as _imp
from collections import namedtuple as _nt
def pep(n: int):
    if (not isinstance(n, int)) or n < 0 or n > 9999:
        raise ValueError(f'Invalid PEP number {n!r}')
    try:
        return _imp.import_module(f'pep{n}', '.')
    except ImportError:
        raise ValueError(f'PEP {n!r} not supported') from None
pepinfo = _nt('pepinfo', ('number', 'title', 'status', 'creation', 'url'))
def info(n: int):
    doc = pep(n).__doc__.splitlines()
    if doc is None:
        raise NotImplementedError(f'Info of PEP {n!r} unavailable')
    return pepinfo(number=n,
                   title=doc[2].split(' -- ')[1],
                   status=doc[3].lstrip('Status: '),
                   creation=doc[4].lstrip('Created: '),
                   url=f'https://www.python.org/dev/peps/pep-{n:0>4}/')

SUPPORTED = frozenset((212, 265, 276, 303,
                       326, 351, 416, 559))
# No auto because it's too slow