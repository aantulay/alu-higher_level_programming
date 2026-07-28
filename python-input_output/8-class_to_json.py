#!/usr/bin/python3
"""Module that defines a function to build a JSON-serializable dict."""


def class_to_json(obj):
    """Return the dictionary description of a simple-data-structure object.

    Args:
        obj: An instance of a class whose attributes are limited to
            lists, dictionaries, strings, integers, and booleans.

    Returns:
        dict: A shallow copy of obj's instance attribute dictionary,
        suitable for JSON serialization.
    """
    return obj.__dict__
