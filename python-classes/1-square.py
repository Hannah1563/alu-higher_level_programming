#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""

class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the new Square.
        """
        self.__size = size
