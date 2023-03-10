#!/usr/bin/python3
"""module for base class"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """base class defination"""
    def __init__(self, *args, **kwargs):
        """base class initalization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, value)

    def __str__(self):
        """return a string"""
        return "[{}]({}){}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """upadates the atrributes"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """rteurns a dictionary"""
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        return base_dict
