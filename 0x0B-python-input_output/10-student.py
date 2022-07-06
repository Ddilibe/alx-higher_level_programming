#!/usr/bin/python3
"""
    A module that defines a student class
"""


class Student:
    """
        A student class

        arg: Public instance attributes
            @first_name: The first name of the student
            @last_name: The last name of the student
            @age: The age of the student
    """
    def __init__(self, first_name, last_name, age):
        """ Initializing the class with the attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that retreives a dictionary representation of a student """
        if attrs is not None:
            new_dict = {}
            if type(attrs) == list:
                for i in attrs:
                    if i in self.__dict__:
                        new_dict[i] = self.__dict__[i]
            else:
                new_dict[attrs] = self.__dict__[attrs]
            return (new_dict)
        return (self.__dict__)
