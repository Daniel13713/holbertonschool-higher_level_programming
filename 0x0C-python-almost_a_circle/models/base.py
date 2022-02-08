#!/usr/bin/python3
"""This module have the Mother class Base"""


from fileinput import filename
import json
import csv


class Base:
    """Class Base
    Arg:
        -class attribute
        -"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor with only id instance"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json representation string"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:
        """
        if list_objs is None or len(list_objs) == 0:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            obj_json = cls.to_json_string(list_dict)
            file.write(obj_json)

    @staticmethod
    def from_json_string(json_string):
        """
        from json string to dictionary, Deserialization
        json_string is a string representing a list of dict
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    def dummy(self):
        """Intance to help to create classmethod"""
        if self.__name__ == "Rectangle":
            return self(1, 1, 0, 0, 1)
        elif self.__name__ == "Square":
            return self(1, 0, 0, 1)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        obj = cls.dummy(cls)
        cls.update(obj, **dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                data = file.read()
                dictionaries = cls.from_json_string(data)
                list_objects = [cls.create(**dict) for dict in dictionaries]
                return list_objects
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize in csv"""

        if list_objs is None or len(list_objs) == 0:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        name = cls.__name__
        filename = name + ".csv"
        if name == "Square":
            keys = ["id", "size", "x", "y"]
        elif name == "Rectangle":
            keys = ["id", "width", "height", "x", "y"]
        with open(filename, mode="w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            [writer.writerow(dict) for dict in list_dict]

    @classmethod
    def load_from_file_csv(cls):
        """Deserealitation in csv"""
        count = 0
        list_dict = []
        name = cls.__name__
        filename = name + ".csv"
        with open(filename, mode="r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            print(csv_reader)
            for row in csv_reader:
                if count == 0:
                    keys = row
                else:
                    nums = [int(num) for num in row]
                    list_dict.append(dict(zip(keys, nums)))
                count = count + 1
            list_objects = [cls.create(**dict) for dict in list_dict]

        return list_objects
