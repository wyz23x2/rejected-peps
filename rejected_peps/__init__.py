__version__ = '0.9.1'
import importlib as _imp
from collections import namedtuple as _nt
from itertools import chain as _chain
# Typing
from typing import Generator as _Gen, Optional as _O
from types import ModuleType as _Module

def pep(n: int, *ns, allow_empty: bool = False) -> _Module:
    if not ns:
        if (not isinstance(n, int)) or n < 0 or n > 9999:
            raise ValueError(f'Invalid PEP number {n!r}')
        try:
            try:
                return _imp.import_module(f'..pep{n}', 'rejected_peps.subpkg')
            except ImportError:
                return _imp.import_module(f'pep{n}')
        except ImportError:
            raise ValueError(f'PEP {n!r} not supported') from None
    else:
        try:
            from . import combined
        except ImportError:
            import combined
        ns = frozenset((n, *ns))
        mp = map(str, sorted(ns))
        m = _Module(f'pep' + '_'.join(mp))  # Use := after 3.7 dropped
        v, f = vars(combined), False
        for i in v:
            try:
                if not (getattr(v[i], 'combines') - ns):
                    setattr(m, i, v[i])
                    f = True
            except AttributeError:
                pass
        if not (f or allow_empty):
            raise ValueError('PEPs ' + ', '.join(mp[:-1]) + f' and {mp[-1]} are not supported'
                             'or cannot be combined')
        return m
SUPPORTED = frozenset((204, 211, 212, 259,
                       265, 276, 281, 294,
                       303, 313, 326, 335,
                       336, 349, 351, 416,
                       535, 559, 754, 3140))
# ↑ Not automatic because it's too slow
def search(*s, strict: bool = False) -> _Gen:
    global SUPPORTED
    if not s:
        return
    if any((not isinstance(i, str)) for i in s):
        raise TypeError('Invalid argument(s)')
    func = ((lambda n: n) if strict else str.lower)
    for pep in sorted(SUPPORTED):
        t = info(pep).title
        if all((func(x) in func(t)) for x in s):
            yield pep
def _search_any(*s, strict: bool = False) -> _Gen:
    for i in _chain.from_iterable(search(x, strict=strict) for x in s):
        yield i
search.any = _search_any
def _search_one(*s, strict: bool = True) -> _O[int]:
    global SUPPORTED
    if not s:
        return None
    func = ((lambda n: n) if strict else str.lower)
    xs = []
    for pep in sorted(SUPPORTED):
        t = info(pep).title
        j = 0
        for x in s:
            try:
                j += (func(x) in t.lower() or
                      func(x) in func(t) or
                      func(x) in t.upper())
            except TypeError:
                message = ["args must be type 'str', ",
                           f"not {type(x).__name__!r}"]
                if isinstance(x, bool):
                    message.append(f'. Did you mean strict={x!r}?')
                raise TypeError(''.join(message)) from None
        if j == len(s):
            if not strict:
                return pep
            xs.append(pep)
    if not strict:
        return None
    if xs[1:]:
        raise ValueError(f'More than 1 match: {", ".join(map(str, xs))} ({len(xs)})')
    if not xs:
        raise ValueError(f'No match found')
    return xs[0]
search.one = _search_one
def _search_one_any(*s, strict: bool = True) -> _O[int]:
    global SUPPORTED
    if not s:
        return
    func = ((lambda n: n) if strict else str.lower)
    xs = []
    for pep in sorted(SUPPORTED):
        t = info(pep).title
        for x in s:
            try:
                cond = (func(x) in t.lower() or
                        func(x) in func(t) or
                        func(x) in t.upper())
                if cond:
                    break
            except TypeError:
                message = ["args must be type 'str', ",
                           f"not {type(x).__name__!r}"]
                if isinstance(x, bool):
                    message.append(f'. Did you mean strict={x!r}?')
                raise TypeError(''.join(message)) from None
        else:
            continue
        if not strict:
            return pep
        xs.append(pep)
    if not strict:
        return None
    if xs[1:]:
        raise ValueError(f'More than 1 match: {", ".join(map(str, xs))} ({len(xs)})')
    if not xs:
        raise ValueError(f'No match found')
    return xs[0]
search.one.any = _search_one_any
def get(*s) -> _Module:
    return pep(search.one(*s))
def _get_any(*s) -> _Module:
    return pep(search.one.any(*s))
get.any = _get_any
del _search_any
del _search_one
del _search_one_any
del _get_any

class UnavailableError(LookupError, NotImplementedError):
    pass
pepinfo = _nt('pepinfo', ('number', 'title', 'status', 'creation', 'url'))
def info(n: int) -> pepinfo:
    doc = getattr(pep(n), '__doc__', '').splitlines()
    if not doc[3:]:
        raise UnavailableError(f'Info of PEP {n!r} unavailable')
    return pepinfo(number=n,
                   title=doc[2].split(' -- ')[1],
                   status=doc[3].lstrip('Status: '),
                   creation=doc[4].lstrip('Created: '),
                   url=f'https://peps.python.org/pep-{n:0>4}/')

def __getattr__(name: str):
    if name.startswith('pep'):
        try:
            p = pep(int(name[3:]))
        except (TypeError, ValueError):
            pass
        else:
            return p
    if name.upper() == 'SUPPORTED':
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}. '
                             "Did you mean: 'SUPPORTED'?")
    if name.lower().startswith('info'):
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}. '
                             "Did you mean: 'info'?")
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
def __dir__() -> list:
    return sorted(set(globals().keys()) | {f'pep{n}' for n in SUPPORTED})
