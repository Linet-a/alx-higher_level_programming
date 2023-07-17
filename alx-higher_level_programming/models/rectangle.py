#!/usr/bin/python3
"""
a Rectangle class that inherits from class Base
"""


from models.base import Base


class Rectangle(Base):
    """inherits from the class Base
    attrs:
        __width
        __height
        x
        y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises the new rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init(id) = id

    @property
    def width(self):
        """gets/sets the current width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an interger")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set the height of the triangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets/sets the x coordinates of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an interger")
        elif value < 0:
            raise ValuError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets/sets the y cordintaes of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an interger")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calcuates the area of a recatngle and return the result"""
        return self.width * self.height

    def display(self):
        """prints the Rectangle instance with character "#" """
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Assign arguments to the attributes of the Rectangle."""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary():
        """Returns the dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """prints the string representation of the Rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/\
                                                            {self.height}"
