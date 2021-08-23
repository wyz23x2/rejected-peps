"""\
PEP INFO

PEP 259 -- Omit printing newline after newline
Status: Rejected
Created: 2001-06-11

MODULE INFO

This module provides the print() function that omits the trailing
newline of the last argument if `end` starts with '\\n'.

REFERENCES

PEP 259: <https://www.python.org/dev/peps/pep-0259/>
"""
PEP = 259

import builtins as _b
def print(*args, sep: str = ' ', end: str = '\n', file=None,
          flush: bool = False) -> None:
    if not args:
        return _b.print(sep=sep, end=end, file=file, flush=flush)
    # Use str.removesuffix as soon as support for Python 3.8 is dropped
    if not isinstance(end, (str, type(None))):
        raise TypeError(f'end must be None or a string, '
                        f'not {type(sep).__name__}')
    if str(args[-1]).endswith('\n') and end.startswith('\n'):
        return _b.print(*args[:-1], str(args[-1])[:-1],
                        sep=sep, end=end, file=file, flush=flush)
    return _b.print(*args, sep=sep, end=end, file=file, flush=flush)
