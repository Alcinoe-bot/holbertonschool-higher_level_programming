#!/usr/bin/python3
"""
module 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    return if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
