================
The First Steps
================
Getting Submodules
-------------------
After `installing the package <../quickstart.html>`_, you can get a PEP submodule in several ways::

    >>> import rejected_peps as rp
    >>> p = rp.pep212    # Direct
    >>> p = rp.pep(212)  # Function
    >>> p.indices([1, 2, 3])
    range(0, 3)
    >>> p.PEP  # Get the PEP number through the module
    212

Getting Information
---------------------
You can check the info of a PEP::

    >>> rp.info(212)
    pepinfo(number=212, title='Loop Counter Iteration', status='Rejected', creation='2000-08-22', url='https://peps.python.org/pep-0212/')
    >>> rp.info(754)
    pepinfo(number=754, title='IEEE 754 Floating Point Special Values', status='Rejected', creation='2003-03-28', url='https://peps.python.org/pep-0754/')
    >>> rp.info(204).number
    204
    >>> rp.info(535)[-1]
    'https://peps.python.org/pep-0535/'

Word Searching
----------------
If you forget the PEP number, you can search it::

    >>> list(rp.search('loop'))
    [212, 281]
    >>> list(rp.search('loop', 'range'))  # All
    [281]
    >>> list(rp.search.any('loop', 'range'))  # Any
    [212, 281, 204]
    >>> rp.search.one('loop', 'range')  # Only returns one
    281
    >>> rp.search.one.any('loop', 'range')  # Raises if zero or more than one
    Traceback (most recent call last):
      ...
    ValueError: More than 1 match: 204, 212, 281 (3)

Get the module directly::

    >>> rp.get('loop', 'range').PEP
    281
    >>> rp.get.any('with', 'range').PEP
    281

Now that you know several ways to get a PEP module, you can learn each module now:

.. toctree::
    :glob:
    :name: itoc
    :maxdepth: 2

    pep*
