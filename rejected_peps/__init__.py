__version__ = '0.4.0'
import importlib as _imp
from collections import namedtuple as _nt

def pep(n: int):
    if (not isinstance(n, int)) or n < 0 or n > 9999:
        raise ValueError(f'Invalid PEP number {n!r}')
    try:
        try:
            return _imp.import_module(f'..pep{n}', 'rejected_peps.subpkg')
        except ImportError:
            return _imp.import_module(f'pep{n}')
    except ImportError:
        raise ValueError(f'PEP {n!r} not supported') from None
SUPPORTED = frozenset((204, 211, 212, 259,
                       265, 276, 281, 294,
                       303, 313, 326, 336,
                       349, 351, 416, 559,
                       754, 3140))
# ↑ Not automatic because it's too slow
def search(*s, strict=False):
    global SUPPORTED
    if not s:
        return
    func = ((lambda n: n) if strict else str.lower)
    for pep in sorted(SUPPORTED):
        t = info(pep).title
        if any((func(x) in func(t)) for x in s):
            yield pep
def search_one(*s, strict=True):
    global SUPPORTED
    if not s:
        return
    func = ((lambda n: n) if strict else str.lower)
    xs = []
    for pep in sorted(SUPPORTED):
        t = info(pep).title
        for x in s:
            try:
                if (func(x) in t.lower() or
                    func(x) in func(t) or
                    func(x) in t.upper()):
                    if strict:
                        xs.append(pep)
                    else:
                        return pep
            except TypeError:
                message = ["args must be type 'str', "
                           f"not {type(x).__name__!r}"]
                if isinstance(x, bool):
                    message.append(f'. Did you mean strict={x!r}?')
                raise TypeError(''.join(message)) from None
    if not strict:
        return None
    if xs[1:]:
        raise ValueError(f'More than 1 match: {", ".join(map(str, xs))} ({len(xs)})')
    if not xs:
        raise ValueError(f'No match found')
    return xs[0]
def get(*s):
    return pep(search_one(*s))

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

def __getattr__(name):
    if name.startswith('pep'):
        try:
            p = pep(int(name[3:]))
        except (TypeError, ValueError):
            pass
        else:
            return p
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
def __dir__():
    return sorted(set(globals().keys()) | {f'pep{n}' for n in SUPPORTED})
