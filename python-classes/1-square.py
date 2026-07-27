#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Represent a square.

    This class stores the size of a square as a private instance
    attribute, so the value cannot be accessed directly from outside
    the class.
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
