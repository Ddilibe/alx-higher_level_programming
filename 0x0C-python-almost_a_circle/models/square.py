#!/usr/bin/python3
"""
    Module for a special rectangle where all sides are equal
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """
        Class with the special rectangle called a square
        arge:
            @size: The size of the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing the square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Method that describes details in a class """
        id, x, y, w = self.id, self.x, self.y, self.width
        return "[Square] ({}) {}/{} - {}".format(id, x, y, w)

    @property
    def size(self):
        """ Method to return the size of a square """
        return (self.width)

    @size.setter
    def size(self, value):
        """ Method for setting a value in the square attribute """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Method used to update attributes in a class """
        item = ['id', 'size', 'x', 'y']
        if len(args) > 0:
            for i in range(len(args)):
                try:
                    setattr(self, item[i], args[i])
                except Exception as e:
                    break
        if len(kwargs) > 0:
            try:
                for i, j in kwargs.items():
                    setattr(self, i, j)
            except Exception as e:
                pass

    def to_dictionary(self):
        """ Method that returns the doctionary representation of a square """
        items = ['id', 'x', 'y', 'size']
        dicted = {}
        for i in items:
            dicted[i] = getattr(self, i)
        return (dicted)
