#!/usr/bin/python3
"""
    A module containing a Rectangle class
    The rectangle class inherits from the base
"""


from .base import Base
import sys


class Rectangle(Base):
    """
        Rectangle class that inherits the Base class
        Instance Attributes:
            @__width: COntains the width of the rectangle
            @__height: Contains the height of the rectangle
            @__x: Contains x variable of the rectangle
            @__y: Contains y variable of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantizing the rectangle instance class """
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Method for the getter class for the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Method for the setter class for the width """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ Method for the getter class for the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method for the setter class for the height """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def y(self):
        """ Method for the getter class for the y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Method for the setter class for the y attribute """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """ Method for the getter class for the x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Method for the setter class for the x attribute """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """ Method that returns the area value of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ Method That prints the rectangle in instance
        with the character # """
        q = ""
        for i in range(self.__height):
            for w in range(self.__x):
                q += " "
            for j in range(self.__width):
                q += "#"
            q += "\n"
        sys.stdout.write(q)
        return (q)

    def __str__(self):
        """ Method that is used to describe the rectangle class """
        id, x, y = self.id, self.__x, self.__y
        h, w = self.__width, self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h)

    def update(self, *args, **kwargs):
        """ Method for updating the class attributes"""
        items = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            e = 0
            for i in range(len(args)):
                setattr(self, items[i], args[i])
                if e == 4:
                    break
                e += 1
        if len(kwargs) > 0:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        """ Method the returns the dictionary representation of a rectangle """
        mene = ['x', 'y', 'id', 'height', 'width']
        dicted = {}
        for i in mene:
            dicted[i] = getattr(self, i)
        return (dicted)
