#!/usr/bin/python3
"""
Rectangle  class definition
"""


class Rectangle:
    """class representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """initialises the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be a interger")
        self.__width = value

    @property
    def height(self):
        """getter for the private attibute height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an interger")
        self.__height = value
