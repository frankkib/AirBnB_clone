#!/usr/bin/pyhton3
from models.base_model import BaseModel
"""class state module"""


class State(BaseModule):
    """class representaion"""
    name = ""

    def __init__(self, *args, **kwargs):
        """class initialization"""
        super().__init__(*args, **kwargs)
