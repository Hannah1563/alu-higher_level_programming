#!/usr/bin/python3
"""
Module containing the Rectangle class that inherits from BaseGeometry.
"""
from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class that defines a Rectangle, inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
