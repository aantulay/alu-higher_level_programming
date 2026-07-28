#!/usr/bin/python3
"""Module that defines a Student class that can serialize and reload."""


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

    def to_json(self, attrs=None):
        """Return a dictionary representation of this Student instance.

        Args:
            attrs (list): An optional list of attribute-name strings.
                If given, only matching attributes are returned.
                Otherwise every attribute is returned.

        Returns:
            dict: The filtered (or full) dictionary of attributes.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace this Student instance's attributes from a dictionary.

        Args:
            json (dict): A mapping of attribute names to new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
