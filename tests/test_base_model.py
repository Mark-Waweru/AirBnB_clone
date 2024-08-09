#!/usr/bin/python3
'''This module is for testing the BaseModel class in base_model.py file'''
import unittest
import uuid
from datetime import datetime, timedelta
from models.base_model import BaseModel
import re


class Test_BaseModel(unittest.TestCase):
    '''This is a Test class for the BaseModel class and it has some
    test edge cases
    '''
    def setUp(self):
        '''This setUp method defines the instances of the BaseModel class'''
        self.test_model = BaseModel()
        self.test_model.name = "My test Model Object"
        self.test_model.number = 100

    def test_init_method(self):
        '''This method tests the init method of BaseModel if it converts
        the dictionary json back to an instance object
        '''
        test_model_json = self.test_model.to_dict()
        new_test_model = BaseModel(**test_model_json)
        obj_class_name = test_model_json["__class__"]
        self.assertIsInstance(new_test_model.created_at, datetime)
        self.assertIsInstance(new_test_model.updated_at, datetime)
        self.assertIsNot(self.test_model, new_test_model)
        self.assertEqual(new_test_model.__class__.__name__, obj_class_name)

    def test_uuid4(self):
        '''This method test if id is a valid UUID4'''
        self.assertIsInstance(self.test_model.id, str)
        uuid_pattern = re.compile(
        r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-'
        r'[89abAB][a-f0-9]{3}-[a-f0-9]{12}$'
        )
        self.assertTrue(uuid_pattern.match(self.test_model.id))

    def test_created_at(self):
        '''This method test that created_at is a datetime and close to now'''
        self.assertIsInstance(self.test_model.created_at, datetime)
        self.assertAlmostEqual(self.test_model.created_at, datetime.now(),
                delta = timedelta(seconds = 1))

    def test_updated_at(self):
        '''This method test that updated_at is a datetime and close to now'''
        self.assertIsInstance(self.test_model.updated_at, datetime)
        self.assertAlmostEqual(self.test_model.updated_at, datetime.now(),
                delta = timedelta(seconds = 1))

    def test_str_method(self):
        '''This method test the BaseModel __str__ method if it outputs
        [<class name>] (<self.id>) <self.__dict__> when called
        '''
        expected_output = "[{}] ({}) {}".format(
            self.test_model.__class__.__name__, self.test_model.id,
            self.test_model.__dict__)
        self.assertEqual(str(self.test_model), expected_output)

    def test_save_method(self):
        '''This method test the BaseModel Save method if the updated_at
        time is recorded and updated correctly
        '''
        old_updated_at = self.test_model.updated_at
        self.test_model.save()
        self.assertGreater(self.test_model.updated_at, old_updated_at)
        self.assertAlmostEqual(self.test_model.updated_at, datetime.now(),
            delta = timedelta(seconds = 1))

    def test_to_dict_method(self):
        '''This method tests the BaseModel to_dict method to ensure it returns
        a correct dictionary representation of the instance
        '''
        obj_dict = self.test_model.to_dict()
        self.assertEqual(obj_dict["id"], self.test_model.id)
        self.assertEqual(obj_dict["__class__"],
            self.test_model.__class__.__name__)
        self.assertEqual(obj_dict["created_at"],
            self.test_model.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"],
            self.test_model.updated_at.isoformat())
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

    def tearDown(self):
        '''This tearDown method deletes the instances of the BaseModel class
        '''
        del self.test_model

if __name__ == "__main__":
    unittest.main()
