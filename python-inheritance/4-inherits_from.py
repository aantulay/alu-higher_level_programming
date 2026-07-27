#!/usr/bin/python3
"""Module that defines a function to check strict inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj's class inherited from a_class.

    Unlike is_kind_of_class, an obj that is a direct instance of
    a_class itself does not count; only true subclasses do.

    Args:
        obj: The object to check.
        a_class (type): The class obj's class must inherit from.

    Returns:
        bool: True if obj's type is a strict subclass of a_class,
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
