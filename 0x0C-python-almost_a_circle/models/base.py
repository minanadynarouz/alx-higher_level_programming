#!/usr/bin/python3

"""Module base
Defines a Base class for other classes in the project
"""

import json
import os


class Base:
    """Base class
    Private class attribute: __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of a Base instance
        Args:
        - id: id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Update JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        jsonFile = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        dicts_list = []
        with open(jsonFile, 'w') as f:
            for i in list_objs:
                dicts_list.append(i.to_dictionary())
            f.write(cls.to_json_string(dicts_list))

    @staticmethod
    def from_json_string(json_string):
        """represent list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Update instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            newObj = cls(2, 3)
        elif cls.__name__ == "Square":
            newObj = cls(1)

        newObj.update(**dictionary)
        return newObj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        fileName = cls.__name__ + ".json"

        if not os.path.exists(fileName):
            return []
        with open(fileName, 'r') as f:
            listsObj = cls.from_json_string(f.read())
        list = []
        for dict in listsObj:
            list.append(cls.create(**dict))
        return list


    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if list_objs:
                for obj in list_objs:
                    writer.writerow([getattr(obj, attr) for attr in obj.get_attributes()])
            else:
                writer.writerow([])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                obj_list = []
                for row in reader:
                    if row:
                        obj_dict = {}
                        for i, attr in enumerate(cls.get_attributes()):
                            obj_dict[attr] = int(row[i])
                        obj_list.append(cls.create(**obj_dict))
                return obj_list
        except FileNotFoundError:
            return []


            @staticmethod
    def draw(list_rectangles, list_squares):
        turt = turtle.Turtle()
        turt.screen.bgcolor("lightblue")
        turt.pensize(5)
        turt.shape("turtle")
        turt.penup()
        turt.pendown()
        turt.speed(6)

        window_width = turtle.window_width()
        window_height = turtle.window_height()

        turt.color("darkgreen")
        for re in list_rectangles:
            window_width += 40
            window_height += 50
            turt.showturtle()
            turt.penup()
            turt.pendown()
            for _ in range(2):
                turt.forward(re.width)
                turt.right(90)
                turt.forward(re.height)
                turt.right(90)
            turt.penup()
            turt.setpos(-window_width / 4, window_height / 6)
            turt.hideturtle()

        turt.color("purple")
        for sq in list_squares:
            turt.showturtle()
            turt.penup()
            turt.pendown()
            for _ in range(2):
                turt.forward(sq.width)
                turt.right(90)
                turt.forward(sq.height)
                turt.right(90)
            turt.penup()
            turt.setpos(-window_width / 10, window_height / 20)
            turt.hideturtle()
        turtle.done()
