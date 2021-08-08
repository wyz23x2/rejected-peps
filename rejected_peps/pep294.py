"""\
PEP INFO

PEP 294 -- Type Names in the types Module
Status: Rejected
Created: 2002-06-19

MODULE INFO

This module adds the lowercase regular version as in the PEP to 
the types module and this module. If the new name is invalid 
(e.g. `lambda`), a trailing underscore is added.

REFERENCES

PEP 294: <https://www.python.org/dev/peps/pep-0294/>
"""
import types
for name in dir(types):
    if name[-4:] == 'Type' and name[:-4]:
        new_name = name[:-4].lower()
        if not new_name.isidentifier():
            new_name = f'{new_name}_'
        globals()[new_name] = getattr(types, name)
        setattr(types, new_name, getattr(types, name))
