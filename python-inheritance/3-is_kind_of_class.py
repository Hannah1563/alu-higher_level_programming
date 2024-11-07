#!/usr/bin/python3
"""
Module containing a function that checks if an object is an instance of, or
an instance of a class that inherited from, the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or an instance of a class
    that inherited from, the specified class. Otherwise, returns False.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an instance of, or an instance of a class
        that inherited from, the specified class. False otherwise.
    """
    return isinstance(obj, a_class)
