#!/usr/bin/python3
'''
class to define all class and models
'''
from uuid import uuid4
from datetime import datetime as dt
import models


class BaseModel:
    '''method definition for other classes'''

    def __init__(self, *args, **kwargs):
        '''initialisation'''
        self.id = str(uuid4())
        self.created_at = dt.now()
        self.updated_at = self.created_at

        if kwargs:
            for key in kwargs:
                if key in ["created_at",
                           "updated_at"]:
                    self.__dict__[key] = dt.strptime(kwargs[key], "%Y-%m-%dT%H"
                                                                  ":%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            models.storage.new(self)

    def __str__(self):
        '''string rep'''
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''saving updates'''
        self.updated_at = dt.now()

    def to_dict(self):
        '''dictionary rep'''
        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = self.__class__.__name__
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        return copy_dict
