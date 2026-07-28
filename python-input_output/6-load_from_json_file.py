#!/usr/bin/python3
"""Module that defines a function to load an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create an object from the JSON representation stored in a file.

    Args:
        filename (str): The path of the file to read from.

    Returns:
        The Python object represented by the file's JSON content.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
