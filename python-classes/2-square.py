#!/usr/bin/python3
"""Defines a Square class with a private size attribute and size validation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the new Square. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise
