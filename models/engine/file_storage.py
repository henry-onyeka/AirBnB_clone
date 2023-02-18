
# !/usr/bin/python3
"""Inside the file_storage module."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Inside the FileStorage class.
    Attrs:
        __file_path (str): Path to json file.
        __objects (dict): Dict to store objs.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name, obj.id)] = obj

    def save(self):
        """erializes __objects to the JSON file (path: __file_path)"""
        my_dict = FileStorage.__objects
        new_dict = {key: my_dict[key].to_dict() for key in my_dict}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects
         (only if the JSON file (__file_path) exists."""
        try:
            with open(FileStorage.__file_path) as file:
                my_dict = json.load(file)
                for v in my_dict.values():
                    name_cls = v['__class__']
                    del v['__class__']
                    self.new(eval(name_cls)(**v))
        except FileNotFoundError:
            return
