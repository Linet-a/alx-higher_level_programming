#!/usr/bin/python3
"""
Rectangle class definition
"""


class Rectangle:
    """class representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self._width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if isinstance(value, int):
            if value >= 0:
                self._width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """getter for the private attribute height"""
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self._height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

