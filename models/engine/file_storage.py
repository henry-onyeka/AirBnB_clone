#!/usr/bin/python3
'''class to store datas by instantiting'''
import sys
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models

class FileStorage:
    '''converts dictionary to json file and vise versa'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''this returns dictionary'''
        return self.__objects


    def new(self, obj):
        """ sets the __objects the obj with class name and id """
        new_1 = obj.__class__.__name__
        new_2 = obj.id
        new = new_1 + '.' + new_2
        self.__objects[new] = obj

    def save(self):
        '''serialisation of the dictionarty to json file and saving into local storage'''
        d_info = {}
        with open(self.__file_path, 'w') as f:
            for k, va in self.__objects.items():
                d_info[k] = va.to_dict()
                json.dump(d_info, f)

    def reload(self):
        """ deserialization """
        classes = {'BaseModel': BaseModel,
                   'User': User, 'Place': Place,
                   'State': State, 'City': City,
                   'Amenity': Amenity, 'Review': Review}

        try:
            with open(self.__file_path, 'r') as f1:
                file_store = json.load(f1)
                for k, va in file_store.items():
                    if '__class__' in va:
                        val = classes[va['__class__']](**va)
                        self.__objects[k] = val
        except:
            pass
