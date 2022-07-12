#!/usr/bin/python3
"""
    Module containing the base class for all other classes
"""


import json


class Base:
    """
        A base class built for all other class

        Args:
            Class Attribute:
                @__nb_objects: Number of classes instantiazed
            Instance Attribute:
                @id: Id of the instantized element
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantizing the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method the returns the JSON string representation of
        a dictionary """
        if list_dictionaries is None:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Method that writes the JSON string representation
        of the argument in to a file """
        h = []
        if list_objs is not None:
            for i in list_objs:
                d = i.to_dictionary()
                h.append(d)
        h = cls.to_json_string(h)
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(h)

    @staticmethod
    def from_json_string(json_string):
        """ Method that returns the list of the JSON string representation """
        if json_string is not None or len(json_string) > 0:
            h = json.loads(json_string)
            return (h)
        return ([])

    @classmethod
    def create(cls, **dictionary):
        """ Method that returns an instance with all attributes already set """
        w = cls(1, 1)
        w.update(**dictionary)
        return (w)

    @classmethod
    def load_from_file(cls):
        """ Method that returns a list of instances """
        w = []
        with open("{}.json".format(cls.__name__), "r") as f:
            e = json.load(f)
            for i in e:
                i = cls.to_json_string(i)
                i = cls.from_json_string(i)
                q = cls.create(**i)
                w.append(q)
            return (w)
        return (list())
