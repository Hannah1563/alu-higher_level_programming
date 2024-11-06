#!/usr/bin/python3
"""
This module defines a Rectangle class with width, height,
area, perimeter calculation, customizable print symbol,
and instance tracking.
"""


class Rectangle:
    """
    Rectangle class that defines a rectangle by width and height,
    includes methods for calculating area and perimeter, supports
    printing a visual representation using a specified symbol, and
    tracks the number of instances.
    """

    number_of_instances = 0  # Tracks the number of Rectangle instances
    print_symbol = "#"  # Symbol for string representation of the rectangle

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance with width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment instance count

    @property
    def width(self):
        """Getter for width."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for width with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter for height."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for height with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculate the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        Returns:
            int: The perimeter of the rectangle. If width or height is zero,
                 perimeter is zero.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle using `print_symbol`.
        Returns:
            str: A string representing the rectangle. Empty string if width
                 or height is zero.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """
        Return a string representation for recreating a new instance.
        Returns:
            str: String format 'Rectangle(width, height)'.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted and
        decrement the instance count.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement instance count
