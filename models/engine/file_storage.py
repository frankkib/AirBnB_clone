#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.city import City


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all the objects"""
        return self.__objects

    def new(self, obj):
        """creating a new dictionary for key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes obejcts to json file"""
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError as Error:
            pass
