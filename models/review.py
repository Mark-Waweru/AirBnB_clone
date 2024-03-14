#!/usr/bin/python3
'''This is a module containing the class Review which inherits from BaseModel
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''A class called Review

    Attributes:
        place_id (str): The place.id
        user_id (str): The user who has reviewed
        text (str): The review text
    '''
    place_id = ""
    user_id = ""
    text = ""
