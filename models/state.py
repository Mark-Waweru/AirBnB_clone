#!/usr/bin/python3
'''A module with a class called State that inherits from BaseModel'''
from models.base_model import BaseModel


class State(BaseModel):
    '''A Class called State

    Attributes:
        name (str): The name of the state
    '''
    name = ""
