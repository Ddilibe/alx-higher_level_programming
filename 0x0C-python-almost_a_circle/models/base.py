#!/usr/bin/python3
"""
    Module containing the base class for all other classes
"""


import json
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that serializes content and saves it to CSV file """
        with open("{}.csv".format(cls.__name__), "w", newline="") as f:
            doing = csv.DictWriter(f, list_objs[0].to_dictionary().keys())
            doing.writeheader()
            for i in list_objs:
                w = i.to_dictionary()
                doing.writerow(w)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that creates instances of the class using deserializes
        data from CSV data file """
        q = []
        with open("{}.csv".format(cls.__name__)) as f:
            doing = csv.DictReader(f)
            for i in doing:
                for keys, values in i.items():
                    if keys != "id":
                        i[keys] = int(values)
                w = cls.create(**i)
                q.append(w)
        return (q)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Method that opens a window and draws all the rectangles
        and squares """
        w, q, f = turtle.Turtle(), 0, 0
        color = ['blue', 'green', 'yellow', 'purple', 'violet', 'indigo', 'red']
        all_list = [list_rectangles, list_squares]
        for j in all_list:
            for i in j:
                w.setposition(i.x, i.y)
                w.pendown()
                w.color(color[f])
                w.begin_fill()
                while q < 2:
                    w.forward(i.width)
                    w.left(90)
                    w.forward(i.height)
                    w.left(90)
                    q += 1
                w.end_fill()
                f += 1
                if f == len(color):
                    f = 0
                f += 1
                q = 0
                w.penup()
        turtle.mainloop()
