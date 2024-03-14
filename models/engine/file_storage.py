#!/usr/bin/python3
'''This module ahs a class `FileStorage` that
serializes instances to a JSON file and deserializes JSON file to instances'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    '''serializes instances to a JSON file and
    deserializes JSON file to instances

    Attributes:
        __file_path (str): The file path for where the data will be stored
        __objects (dict): A dictionary to store the object
        by <class_name.id> key
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects

        Returns:
            (dict): returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''Sets in __objects the obj value with the key <obj class_name>.id
        hence the __objects dictionary will contain this key : value form
        `{class_name.id : obj}`

        Args:
            obj (obj): The object to add to the dictionary as a value item
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)
        Note:
            Before serializing the dictionary __objects to the __file_path,
            we first converted the value pair obj to a dictionary using the
            to_dict function from the BaseModel so as to store them as
            dictionary representation with “simple object type”
        '''
        serialized_obj = {}
        for key, value in self.__objects.items():
            serialized_obj[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as my_file:
            json.dump(serialized_obj, my_file)

    def reload(self):
        '''deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        Note:
            When you dessirialize the dictionary to __objects we did:
                1. Got the objects class by evaluating the class_name
                `class_obj = eval(class_name)`
                2. We then create an instance from the class_obj by
                calling the class_obj and passing the Keyworded arguments
                `obj_instance = class_obj(**value)` this is now an object
                3. You then store the object into a dictionary by using
                the previous format of `class_name.id : obj_instance` into
                the __objects dictionary
        '''
        try:
            with open(self.__file_path, mode="r", encoding="UTF-8") as my_file:
                serialized_obj = json.load(my_file)
                for key, value in serialized_obj.items():
                    class_name, obj_id = key.split('.')
                    class_obj = eval(class_name)
                    obj_instance = class_obj(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
