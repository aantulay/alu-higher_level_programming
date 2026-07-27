#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an unimplemented area."""


class BaseGeometry:
    """Represent a base geometric shape."""

    def area(self):
        """Raise an exception; subclasses must implement this method.

        Raises:
            Exception: Always, with the message
                "area() is not implemented".
        """
        raise Exception("area() is not implemented")
    