#!/usr/bin/python3
"""Module that defines a Square class based on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, built on top of the Rectangle class."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The width and height of the square. Must be
                a positive integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
