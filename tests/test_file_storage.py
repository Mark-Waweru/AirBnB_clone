#!/usr/bin/python3
'''This module is for testing the FileStorage class which does
the serialization and deserialization of the BaseModel objects and its
child class objects to a file.json file.
'''
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models import storage
import unittest
import tempfile
import os


class Test_FileStorage(unittest.TestCase):
    '''Contains TestCases for the FileStorage class'''
    def setUp(self):
        '''Defines/initializes an instance of the BaseModel class or
        its child classes
        '''
        storage._FileStorage__objects = {}
        self.base_model_obj = BaseModel()
        self.base_model_obj.name = "BaseModel object"
        self.base_model_obj.number = 100

        self.child_obj = State()
        self.child_obj.name = "ChildModel object"
        self.child_obj.number = 200

        base_key = "{}.{}".format(self.base_model_obj.__class__.__name__,
                self.base_model_obj.id)
        child_key = "{}.{}".format(self.child_obj.__class__.__name__,
                self.child_obj.id)

        self.temp_file = tempfile.NamedTemporaryFile(delete = False)
        '''This line assigns the temp_file_path the path to the temp file'''
        self.temp_file_path = self.temp_file.name
        self.temp_file.close()

        '''This line below backups the original path of the file.json'''
        self.original_file_path = storage._FileStorage__file_path
        storage._FileStorage_file_path = self.temp_file_path


    def test_new_method(self):
        '''Tests if the new method saves the new objects inside the __objects
        attribute dictionary in the right way and also if it is accurate
        '''
        self.assertIn(child_key, storage._FileStorage__objects)
        self.assertEqual(storage._FileStorage__objects[base_key],
                self.base_model_obj)
        self.assertEqual(storage._FIleStorage__objects[child_key],
                self.child_obj)

    def test_all_method(self):
        '''Test the all method if it returns the objects created and if
        it records all the objects created
        '''
        all_objects = storage.all()
        self.assertEqual(all_objects[base_key], self.base_model_obj)
        self.assertEqual(all_objects[child_key], self.child_obj)
        self.assertEqual(len(all_objects), 2)

        
    def test_save_method(self):
        '''This method tests if the save method serializes the objects well'''
        self.base_model_obj.save()
        self.child_obj.save()

        with open(self.temp_file_path, mode="r") as my_file:
            data = json.load(my_file)

        self.assertIn(base_key, data)
        self.assertIn(child_key, data)
        self.assertEqual(data[base_key], self.base_model_obj.to_dict())
        self.assertEqual(data[child_key], self.child_obj.to_dict())


    def test_reload(self):
        '''Tests the reload method if it desirializes the json file well'''
        self.base_model_obj.save()
        self.child_obj.save()

        self.storage.reload()

        self.assertIn(base_key, storage._FileStorage__objects)
        self.assertIn(child_key, storage._FileStorage__objects)
        self.assertEqual(storage._FileStorage__objects[base_key],
                self.base_model_obj.to_dict())
        self.assertEqual(storage._FileStorage__objects[child_key],
                self.child_obj.to_dict())


    def test_reload_non_existent_file(self):
        '''Test the reload method when the file does not exist.'''

        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)

        self.storage.reload()

        self.assertEqual(self.storage._FileStorage__objects, {})


    def tearDown(self):
        '''This method deletes the instances of the classes created'''
        del self.base_model_obj
        del self.child_obj
        del base_key
        del child_key

        storage._FileStorage__file_path = self.original_file_path

        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)


if __name__ == "__main__":
    unittest.main()
