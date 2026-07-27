#!/usr/bin/python3
"""Module that defines a MyList class based on the list type."""


class MyList(list):
    """A list that can also print its elements in sorted order."""

    def print_sorted(self):
        """Print the list in ascending sorted order.

        The underlying list itself is left unmodified.
        """
        print(sorted(self))