#!/usr/bin/pyhton3
from models.base_model import BaseModel
"""class city module"""


class City(BaseModel):
    """class representation"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """class initializatio"""
        super().__init__(*args, **kwargs)
