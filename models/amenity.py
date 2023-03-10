#!/usr/bin/pyhton3
from models.base_model import BaseModel
"""class amenity module"""


class Amenity(BaseModel):
    """class represenation"""
    name = ""

    def __init__(self, *args, **kwargs):
        """class initialization"""
        super().__init__(*args, **kwargs)
