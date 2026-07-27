#!/usr/bin/python3
"""Module that defines a Rectangle class with a customizable print symbol."""


class Rectangle:
    """Represent a rectangle.

    The width and height are stored as private instance attributes,
    accessible and settable through property getters and setters.
    The class computes area and perimeter, prints itself using the
    class-level `print_symbol` attribute, produces an eval-friendly
    repr, announces when an instance is deleted, and keeps a running
    count of how many instances currently exist.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and count it.

        Args:
            width (int): The width of the new rectangle. Defaults to 0.
            height (int): The height of the new rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        Returns:
            int: 0 if either width or height is 0, otherwise the
            perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the rectangle drawn with `print_symbol`.

        Returns:
            str: An empty string if width or height is 0, otherwise
            `height` rows of `width` copies of `print_symbol`,
            separated by newlines.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.__width
             for _ in range(self.__height)]
        )

    def __repr__(self):
        """Return a string representation that can recreate the rectangle.

        The result is valid Python code such that
        `eval(repr(instance))` produces an equivalent Rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and decrement the instance count on deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
