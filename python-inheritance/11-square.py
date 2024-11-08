#!/usr/bin/python3
"""Module for Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize Square instance
        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate area of Square
        Returns:
            int: area of square
        """
        return self.__size ** 2

    def __str__(self):
        """Return string representation of Square
        Returns:
            str: formatted string with square description
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
