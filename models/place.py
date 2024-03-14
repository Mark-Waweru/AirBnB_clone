#!/usr/bin/python3
'''A module that contains a class called Place that inherits from BaseModel'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''A class called Place

    Attributes:
        city_id (str): It is the City.id of the Place
        user_id (str): It is the User.id of the Place
        name (str): The name of the place
        description (str): The description of the place
        number_rooms (int): The number of rooms the place has
        number_bathrooms (int): The number of bathrooms the place has
        max_guest (int): The maximum number of guests the palce can hold
        price_by_night (int): The Amount charged per night
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_ids (list, str): A list of Amenity.id
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_quest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
