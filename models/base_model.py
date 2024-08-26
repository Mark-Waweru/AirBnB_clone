#!/usr/bin/python3
'''This module has a class BaseModel that defines all common
attributes/methods for other classes'''
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    '''Defines all common attributes/methods for other classes

    Attributes:
        id (str): A unique id for an instance(object)
        created_at (str): The time the instance(object) was created
        updated_at (str): The time the instance(object) was updated
    '''
    def __init__(self, *args, **kwargs):
        '''Initializes the instances with this id, created_at, updated_at
        attributes
        OR
        Creates an instance form a dictionary passed with the **kwargs

        Args:
            *args (object): Any data type object(unlimited)
            **kwargs (dictionery): Unlimited number of  dictionarys
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''print: [<class name>] (<self.id>) <self.__dict__>

        Returns:
            [<class name>] (<self.id>) <self.__dict__>
        '''
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        '''updates the public instance attribute updated_at with the current
        datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__
        of the instance

        Returns:
            a dictionary containing all keys/values of __dict__ of the instance
        '''
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
