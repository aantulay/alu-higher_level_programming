#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization support."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self):
        """Return a dictionary representation of this Student instance."""
        return self.__dict__
