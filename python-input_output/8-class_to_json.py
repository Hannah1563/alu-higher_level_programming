#!/usr/bin/python3
"""Task 8"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure (list,
    dictionary, string, integer, and boolean) for JSON serialization.
    Args:
        obj (object): The instance of the class to be serialized.
    Returns:
        dict: A dictionary containing the serializable attributes.
    """
    return {attr: value for attr, value in obj.__dict__.items()
            if isinstance(value, (str, int, bool, list, dict))}
