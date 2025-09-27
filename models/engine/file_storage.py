#!/usr/bin/python3
"""
FileStorage engine for AirBnB clone project.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes back"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key, obj in FileStorage.__objects.items():
            json_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if file exists)"""
        try:
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, "r") as f:
                    json_objects = json.load(f)
                    for key, value in json_objects.items():
                        class_name = value["__class__"]
                        obj = eval(class_name)(**value)
                        FileStorage.__objects[key] = obj
        except Exception:
            pass
