#!/usr/bin/python3

"""user class"""
from models import base_model


class User(base_model.BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
