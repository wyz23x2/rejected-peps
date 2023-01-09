__version__ = '1.0.0dev2'
import importlib as _imp
import warnings as _w
from collections import namedtuple as _nt
from itertools import chain as _chain
from functools import lru_cache as _lc
# Typing
from typing import Generator as _Gen, Optional as _O
from types import ModuleType as _Module

SUPPORTED = frozenset((204, 211, 212, 259,
                       265, 276, 281, 294,
                       303, 313, 326, 335,
                       336, 349, 351, 416,
                       535, 559, 754, 3140))
# ↑ Not automatic because it's too slow

_pep_imported = {}
def pep(n: int, *ns, allow_empty: bool = False) -> _Module:
    """Return a pep module based on the pep number(s).

    If a single number is provided, the corresponding module is returned.

    If several numbers are provided, a namespace containing the combined objects is returned;
    if there are none, an error is raised unless `allow_empty=True`, where an empty
    namespace is returned.
    """
    if not ns:
        if n in _pep_imported:
            return _pep_imported[n]
        if (not isinstance(n, int)) or n < 0 or n > 9999:
            raise ValueError(f'Invalid PEP number {n!r}')
        try:
            try:
                md =  _imp.import_module(f'..pep{n}', 'rejected_peps.subpkg')
            except ImportError:
                md = _imp.import_module(f'pep{n}')
            _pep_imported[n] = md
            return md
        except ImportError:
            raise ValueError(f'PEP {n!r} not supported') from None
    else:
        try:
            from . import combined
        except ImportError:
            import combined
        combined = _imp.reload(combined)
        ns = frozenset((n, *ns))
        mp = map(str, sorted(ns))
        m = _Module(f'pep' + '_'.join(mp))  # Use := after 3.7 dropped
        v, f = vars(combined), False
        for i in v:
            try:
                if not (getattr(v[i], 'combines') - ns):  # If .combines is a subset of ns
                    setattr(m, i, v[i])
                    f = True
            except AttributeError:
                pass
        if not (f or allow_empty):
            raise ValueError('PEPs ' + ', '.join(mp[:-1]) + f' and {mp[-1]} are not supported'
                             'or cannot be combined')
        return m

@_lc(maxsize=64, typed=True)
def search(*s, strict: bool = False) -> _Gen:
    """Return the numbers of PEPs that have a title or registered name matching *all* the keywords.

    If `strict=True` (default False), the search is case sensitive.
    """
    global SUPPORTED
    if not s:
        return  # Empty
    if any((not isinstance(i, str)) for i in s):
        raise TypeError('Invalid argument(s)')
    yielded = set()
    func = ((lambda n: n) if strict else str.casefold)
    for pep in sorted(SUPPORTED):
        t = info(pep).title
        if all((func(x) in func(t)) for x in s):
            yield pep
            yielded.add(pep)
    for k in s:
        if k in _reg and _reg[k] not in yielded:
            yield _reg[k]

@_lc(maxsize=64, typed=True)
def _search_any(*s, strict: bool = False) -> _Gen:
    """Return the numbers of PEPs that have a title or registered name matching *any* of the keywords.

    If `strict=True` (default False), the search is case sensitive.
    """
    yielded = set()
    for i in _chain.from_iterable(search(x, strict=strict) for x in s):
        if i not in yielded:
            yield i
            yielded.add(i)
search.any = _search_any

@_lc(maxsize=64, typed=True)
def _search_one(*s, strict: bool = True) -> _O[int]:
    """Return the number of the PEP that has a title or registered name matching *all* the keywords.
    If zero or several PEPs are found, an error is raised.
    If `strict=True` (default False), the search is case sensitive.
    """
    global SUPPORTED
    if not s:
        return None
    func = ((lambda n: n) if strict else str.casefold)
    xs = []
    for pep in sorted(SUPPORTED):
        t = info(pep).title
        j = 0
        for x in s:
            try:
                j += (func(x) in t.lower() or
                      func(x) in func(t) or
                      func(x) in t.upper() or
                      _reg.get(func(x), -1) == pep)
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

@_lc(maxsize=64, typed=True)
def _search_one_any(*s, strict: bool = True) -> _O[int]:
    """Return the number of the PEP that has a title or registered name matching *any* of the keywords.
    If zero or several PEPs are found, an error is raised.
    If `strict=True` (default False), the search is case sensitive.
    """
    global SUPPORTED
    if not s:
        return None
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

@_lc(maxsize=64, typed=True)
def get(*s) -> _Module:
    """Return the module of the PEP that has a title matching *all* the keyword(s).
    If zero or several PEPs are found, an error is raised.
    If `strict=True` (default False), the search is case-sensitive.
    """
    return pep(search.one(*s))
@_lc(maxsize=64, typed=True)
def _get_any(*s) -> _Module:
    """Return the module of the PEP that has a title matching *any* of the keyword(s).
    If zero or several PEPs are found, an error is raised.
    If `strict=True` (default False), the search is case-sensitive.
    """
    return pep(search.one.any(*s))
get.any = _get_any

del _search_any
del _search_one
del _search_one_any
del _get_any

_reg = {}
def register(n: int, name: str):
    """Register a name for a PEP number.

    After registering, you can use `rejected_peps.name` or specify it in `search` etc.
    to get the module.
    """
    if __debug__:
        # Specify -O or -OO to improve speed.
        try:
            info(n)
        except (ValueError, UnavailableError):
            raise ValueError(f'Invalid PEP num {n!r}') from None
    if name in _reg and _reg[name] != n:
        raise KeyError(f'Ambiguous keyword {name!r} => {_reg[name]!r} or {n!r}')
    if name.startswith('pep') and name[3:].isdigit():
        _w.warn(f'Name {name!r} conflicts with module {name}; .{name} will return the latter',
                RuntimeWarning, stacklevel=2)
    _reg[name] = n
def unregister(name: str):
    """Unregister a name."""
    del _reg[name]
def clear_register():
    """Clear all registered names."""
    _reg.clear()

class UnavailableError(LookupError, NotImplementedError):
    pass
pepinfo = _nt('pepinfo', ('number', 'title', 'status', 'creation', 'url'))
@_lc(maxsize=32, typed=True)
def info(n: int) -> pepinfo:
    """Return the info of a PEP.

    If the info is unavailable, an UnavailableError is raised.
    """
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
    try:
        p = pep(_reg[name])
    except Exception:
        pass
    else:
        return p
    # Suggestions
    if name.upper() == 'SUPPORTED':
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}. '
                             "Did you mean: 'SUPPORTED'?")
    if name.lower().startswith('info'):
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}. '
                             "Did you mean: 'info'?")
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
def __dir__() -> list:
    return sorted(set(globals().keys()) | {f'pep{n}' for n in SUPPORTED})
