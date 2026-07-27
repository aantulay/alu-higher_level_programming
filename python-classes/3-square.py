#!/usr/bin/python3
"""Module that defines a Square class with an area method."""


class Square:
    """Represent a square.

    The size of the square is validated on instantiation, and the
    class provides a method to compute the area of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size
