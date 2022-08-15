#!/usr/bin/python3

"""Amenity Class which inherits from BaseModel"""
from models import base_model


class Amenity(base_model.BaseModel):
    """Defines the amenity of a Place in AirBnB"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes just like it's parent class BaseModel does"""
        super().__init__(*args, **kwargs)
