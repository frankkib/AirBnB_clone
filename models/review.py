#!/usr/bin/pyhton3
from models.base_model import BaseModel
"""class review module"""


class Review(BaseModel):
    """class review representation"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """class initializatio"""
        super().__init__(*args, **kwargs)
