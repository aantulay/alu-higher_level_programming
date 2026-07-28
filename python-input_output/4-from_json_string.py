#!/usr/bin/python3
"""Module that defines a function to deserialize a JSON string."""
import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to parse.

    Returns:
        The Python data structure represented by my_str.
    """
    return json.loads(my_str)
