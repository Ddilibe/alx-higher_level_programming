#!/usr/bin/python3
class Square:
    """An square class that defines a square

    Args:
        size: The size private instance attribute
        Size is initialized with zero
    """
    def __init__(self, size=0):
        """ Instantizing the class
            
        Attributes:
            size: Size is attribute for the size of the square
            Rasing a type error if size is not an integer
            Rasing a value error if size is less than zero
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ Method for calculating the area of the square class

        Return: The Square area
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Method for retriving the private class"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Method for resetting the private atrribute"""
        self.__size = value
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def __eq__(self, other):
        return self.__size == other.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size
