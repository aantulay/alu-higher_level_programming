#!/usr/bin/python3
"""Module that defines a function to check class membership."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of it.

    Args:
        obj: The object to check.
        a_class (type): The class (or parent class) to compare against.

    Returns:
        bool: True if obj is an instance of a_class, directly or
        through inheritance, False otherwise.
    """
    return isinstance(obj, a_class)
