#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """A class that defines a square with size and position attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square instance
        
        Args:
            size (int): The size of the square (default 0)
            position (tuple): The position of the square (default (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square
        
        Args:
            value (int): The size to set
            
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square
        
        Args:
            value (tuple): The position to set
            
        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square
        
        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters"""
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for i in range(self.__position[1]):
            print()

        # Print the square
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
