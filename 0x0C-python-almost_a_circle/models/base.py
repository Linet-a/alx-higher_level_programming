#!/usr/bin/python3
"""
Represents the base model
Represents the base for all other classes in the pythion project
Attributes:
    __nb_object(int) the number of instantiated Bases
"""

import json


class Base():
    """Represents the base model
    __nb_objects(int):The number of instantiated Bases
    """

    __nb_object = 0

    def __init__(self, id=None):
        """
        initialize a new Base
        Args:
            id(int); the identity of a new Base
        """
        if id not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id += Base.__nb_object


    @staticmethod
    def to_json_string(list_disctionaries):
        """return dictionary serialization of a list of dicts"""
        if list_dictionaries is None or list_dictionaries == []:
            return json.dumps(list_dictionaries)
    

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
