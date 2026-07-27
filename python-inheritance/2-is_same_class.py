#!/usr/bin/python3
"""Module that defines a function to check for an exact class match."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if type(obj) is exactly a_class, False otherwise
        (including when obj is an instance of a subclass of a_class).
    """
    return type(obj) is a_class
