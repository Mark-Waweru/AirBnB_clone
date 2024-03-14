#!/usr/bin/python3
'''A module with a class called city that inherits from BaaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''A class called City

    Attributes:
        state_id (str): The id of the state the city belongs
        name (str): The name of the city
    '''
    state_id = ""
    name = ""
