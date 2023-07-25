"""
Curious about deeper aspects of python, I stumbled upon 
https://github.com/python/cpython/blob/3.11/Lib/asyncio/__init__.py
which was making use of keyword "__all__" & it intrigured me!
"""
# Consider this as AllVariable module

def public_function():
    pass

def _private_function():
    pass

public_variable = 42
_private_variable = 10

__all__ = ['public_function', 'public_variable']

# This will ensure when someone imports from AllVariable.py
# With "from AllVariable import *" only public_function and
# public_variable will be imported for their usability