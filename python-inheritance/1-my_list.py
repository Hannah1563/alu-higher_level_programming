#!/usr/bin/python3
"""Module for class MyList that inherits"""


class MyList(list):
    """Inherits from list and includes a method to print a sorted version."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
