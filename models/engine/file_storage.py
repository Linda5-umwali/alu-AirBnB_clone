#!/usr/bin/python3
"""
FileStorage engine for AirBnB clone project.
"""


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
        pass

    def reload(self):
        """Deserializes the JSON file to __objects (if file exists)"""
        pass
