#!/usr/bin/python3
class Square:
    """An square class that defines a square

    Args:
        size: The size private instance attribute
        Size is initialized with zero
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Instantizing the class
            
        Attributes:
            size: Size is attribute for the size of the square
            Rasing a type error if size is not an integer
            Rasing a value error if size is less than zero
        """
        self.__size = size
        self.__position = position
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
        if (type(self.__position) != tuple or len(position) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')

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

    def my_print(self):
        """Method for printing in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for s in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#",end="")
                print("")

    @property
    def position(self):
        """Method for retrieving the positions private property"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Method for resetting the positions private attribute"""
        self.__position = value
        if (type(self.__position) != tuple or len(position) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
