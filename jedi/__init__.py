"""
Jedi is an autocompletion library for Python. It also offers additional
services such as ``goto``, ``pydoc support`` and ``renaming`` as well as other
IDE helpers.

To give you a simple example how you can use the jedi library, here is an
example for the autocompletion feature:

>>> import jedi
>>> source = '''import json; json.l'''
>>> script = jedi.Script(source, 1, 19, 'example.py')
>>> script
<Script: 'example.py'>
>>> completions = script.complete()
>>> completions
[<Completion: load>, <Completion: loads>]
>>> completions[0].complete
'oad'
>>> completions[0].word
'load'

As you see Jedi is pretty simple and allows you to concentrate on writing a
good text editor, while still having very good IDE features for Python.
"""

import sys

# python imports are hell sometimes. Especially the combination of relative
# imports and circular imports... Just avoid it:
sys.path.insert(0, __path__[0])

from .api import Script, NotFoundError, set_debug_function, _quick_complete
from . import settings

sys.path.pop(0)
