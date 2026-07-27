#!/usr/bin/python3
"""Module that defines a Square class with size and position."""


class Square:
    """Represent a square.

    The square has a validated size and a validated position, and
    can print itself to stdout at that position using the '#'
    character.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.
            position (tuple): The (x, y) position of the square.
                Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: The current (x, y) position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square, with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive
                integers.
        """
        if (type(value) is not tuple or len(value) != 2 or
                not all(type(n) is int and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the '#' character to stdout.

        The square is printed at its stored position: position[1]
        blank lines are printed before the square, and each row is
        indented by position[0] spaces. If the size is 0, prints an
        empty line instead.
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
