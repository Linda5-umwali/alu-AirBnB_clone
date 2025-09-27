#!/usr/bin/python3
"""
BaseModel class for AirBnB clone project.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance"""
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    # Convert string to datetime
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Return string representation of BaseModel"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
