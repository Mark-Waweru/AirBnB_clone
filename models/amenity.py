#!/usr/bin/python3
'''This module has a class called Amenity which inherits from BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''A class called Amenity

    Attributes:
        name (str): The name of the Amenity
    '''
    name = ""
