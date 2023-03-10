#!/usr/bin/pyhton3
from models.base_model import BaseModel

"""User class module"""


class User(BaseModel):
    """class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes class user"""
        super().__init__(*args, **kwargs)
