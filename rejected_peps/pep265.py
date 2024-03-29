from sys import version_info as _vi
__doc__ = ("""\
PEP INFO

PEP 265 -- Sorting Dictionaries by Value
Status: Rejected
Created: 2001-08-08

MODULE INFO

This module implements the sorting function on dicts in PEP 265.
However, its __name__ is changed to itemlist because it returns a list,
not the regular items() type in Python 3. items() is an alias. Also,
since dicts are ordered in supported versions, the sortby argument
accepts -1 (ORIGINAL), 0 (KEYS) and 1 (VALUES).
The `key` and `reverse` parameters are also added to match sorted().
Note that the builtins sorted()
function is more flexable, thus we recommend it instead of itemlist().

REFERENCES

PEP 265: <https://www.python.org/dev/peps/pep-0265/>
Related:""" +
f'\nsorted: <https://docs.python.org/'
f'{".".join(map(str, _vi[:2]))}/library/functions.html#sorted>')
PEP = 265
import builtins as _b

sorted = sorted  # Recommended
def _sort(items: list, index: int, *,
          key=None, reverse: bool = False) -> list:
    if key is None:
        return _b.sorted(items,  # Prevent sorted() overwrite
                         key=(lambda x, i=index: x[i]),
                         reverse=reverse)
    return _b.sorted(items,
                     key=(lambda x, i=index: key(x[i])),
                     reverse=reverse)
ORIGINAL, KEYS, VALUES = -1, 0, 1
# Since dicts are now ordered, an option to not sort is needed
def itemlist(dic, sortby: int = ORIGINAL, *,
             key=None, reverse: bool = False) -> list:
    i = list(dic.items())
    if sortby <= ORIGINAL:
        return (i[::-1] if reverse else i)
    return _sort(i, (not not sortby),
                 key=key, reverse=reverse)
items = itemlist
