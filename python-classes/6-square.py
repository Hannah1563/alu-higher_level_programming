#!/usr/bin/python3
"""a class Square with size and position validation"""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square with size and position validation.
        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        Raises:
            TypeError: If size is not an integer or position is not a tuple
                       of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size  # This calls the size setter for validation
        self.position = position  # This calls the position setter

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation."""
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#'.
        If used to adjust the printing by adding spaces and newlines.
        """
        if self.__size == 0:
            print()
            return

        # Print the newlines according to position[1]
        for _ in range(self.__position[1]):
            print()

        # Print the square with spaces according to position[0]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
