#!/usr/bin/python3
"""Square class definition"""


class Square:
    """ square with size as private instance attribute"""

    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size
        """

        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an interger")
