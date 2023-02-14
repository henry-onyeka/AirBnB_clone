#!/usr/bin/python3
'''Our base model classes for Airbnb project'''

import uuid
from datetime import datetime
import copy
import models
from models.__init__ import storage


class BaseModel:
    ''' we are defining all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''
        created_at: datetime - assign with the current
        datetime when an instance is created
updated_at: datetime - assign with the current datetime
when an instance is created
and it will be updated every time you change your object
        strptime: converts the time into a string format
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            pattern = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                    continue
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, pattern)
                    continue

                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, pattern)
                    continue
                if key != '__class__':
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    models.storage.new(self)

        def __str__(self):
            """ print a readable string """
            return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

        def save(self):
            '''
        updates the saved info with the current time and date it was done
            '''
            self.updated_at = datetime.now()
            models.storage.save()

        def to_dict(self):
            """ returns a dictionary with all keys/value
            of __dict__ of the instance """
            dictnew = copy.deepcopy(self.__dict__)
            dictnew['__class__'] = self.__class__.__name__

            pattern_1 = "%Y-%m-%dT%H:%M:%S.%f"
            dictnew['created_at'] = self.created_at.strftime(pattern_1)
            dictnew['updated_at'] = self.updated_at.strftime(pattern_1)
            dictnew['id'] = self.id
            return dictnew
