#!/usr/bin/python3
"""
Module containing a function that checks if an object is exactly an
instance of a specified class.
"""

def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class,
    and False otherwise.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified class,
        False otherwise.
    """
    return type(obj) is a_class
