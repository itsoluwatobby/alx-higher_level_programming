#!/usr/bin/python3
"""
Defines a class Base
"""
import json
import csv
# import turtle


class Base:
    """
    The base of all the other classes in this project.
    It's main goal is to manage the id attribute in all future classes and to
    avoid duplicating the same code.

    Attributes:
        __nb_objects (int): A private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initiates an instance of a base class

        Args:
            id (int) - an id argument of the base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialized list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        file = cls.__name__ + ".json"
        with open(file, "w") as jsonfileformat:
            if list_objs is None:
                jsonfileformat.write("[]")
            else:
                list_of_dicts = [o.to_dictionary() for o in list_objs]
                jsonfileformat.write(Base.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialized JSON string.

        Args:
            json_string (str): A JSON str the represents of a list of dicts.
        Returns:
            an empty list - If json_string is None or empty.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_dic = cls(1, 1)
            else:
                new_dic = cls(1)
            new_dic.update(**dictionary)
            return new_dic

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of classes that are instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            an empty list - If the file does not exist.
            Otherwise - a list of instantiated classes.
        """
        file = str(cls.__name__) + ".json"
        try:
            with open(file, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        file = cls.__name__ + ".csv"
        with open(file, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writerRow = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writerRow.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of classes that are instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            an empty list - If the file does not exist.
            Otherwise - a list of instantiated classes.
        """
        file = cls.__name__ + ".csv"
        try:
            with open(file, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    #@staticmethod
    #def draw(list_rectangles, list_squares):
    #    """Draws the Rectangles and Squares using turtle module.
    #
    #    Args:
    #        list_rectangles (list): A list of Rectangle objects to draw.
    #        list_squares (list): A list of Square objects to draw.
    #    """
    #    turtl = turtle.Turtle()
    #    turtl.screen.bgcolor("#b7312c")
    #    turtl.pensize(3)
    #    turtl.shape("turtle")

    #    turtl.color("#ffffff")
    #    for rect in list_rectangles:
    #        turtl.showturtle()
    #        turtl.up()
    #        turtl.goto(rect.x, rect.y)
    #        turtl.down()
    #       for i in range(2):
    #            turtl.forward(rect.width)
    #            turtl.left(90)
    #            turtl.forward(rect.height)
    #            turtl.left(90)
    #        turtl.hideturtle()

    #    turtl.color("#b5e3d8")
    #    for sq in list_squares:
    #        turtl.showturtle()
    #        turtl.up()
    #        turtl.goto(sq.x, sq.y)
    #        turtl.down()
    #        for i in range(2):
    #            turtl.forward(sq.width)
    #            turtl.left(90)
    #            turtl.forward(sq.height)
    #            turtl.left(90)
    #        turtl.hideturtle()

    #    turtlel.exitonclick()
