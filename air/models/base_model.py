#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """This is the base model class"""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        Args:
            *args: Unused.
            **kwargs: Dictionary containing attribute
            names and values.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                           value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
