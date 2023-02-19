#!/usr/bin/env python3
"""FileStorage Class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    
    def save(self):
        new_dict = {}

        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()

        with open(self.__file_path, "w+") as f:
            json.dump(new_dict, f, indent=2)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                obj = json.load(f)
            for value in obj.values():
                cls = value["__class__"]
                self.new(eval(cls)(**value))
        except Exception:
            pass
