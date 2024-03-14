#!/usr/bin/python3
'''This module defines a class User that inherits from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''class User that inherits from BaseModel

    Attributes:
        email (str): The email of each user object
        password (str): THe password of each user
        first_name (str): The first name of each user
        last_name (str): The last name of each user
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
