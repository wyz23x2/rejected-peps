=========================
Rejected-PEPs Quickstart
=========================
Installing
------------
First, ensure your Python version is 3.8+:

(Windows)::

    > py -V
    Python 3.11.1

(Others)::

    $ python3 --version
    Python 3.11.1

(Replace ``python3`` with ``py`` below if you use Windows)

Then install it from PyPI::

    $ pip install -U rejected-peps

If you don't have pip, install it first::

    $ python3 -m ensurepip

Check if it's correctly installed::

    >> import rejected_peps as rp
    >>

Importing
-----------

Type ``pepxxx`` to get the module::

    >> rp.pep211
    <module 'rejected_peps.pep211' from '...'>
    >> dir(rp.pep211)
    ['PEP', ..., 'product', 'wrapper']
    >>> rp.pep211.PEP  # Get the PEP number
    211

Or you can use :func:`pep` to get it::

    >> rp.pep(212)
    <module 'rejected_peps.212' from '...'>

Access :attr:`SUPPORTED` to get a frozenset of PEPs supported::

    >> print(*sorted(rp.SUPPORTED), sep=', ')
    204, 211, 212, 259, 265, 276, 281, 294, 303, 313, 326, 335, 336, 349, 351, 416, 535, 559, 754, 3140
