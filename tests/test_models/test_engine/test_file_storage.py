#!/usr/bin/python3
"""
Unittests for FileStorage engine.
"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage"""

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.file_path = "file.json"

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_return_type(self):
        """Test all() returns a dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_creates_key(self):
        """Test new() adds an object"""
        self.storage.new(self.base_model)
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.base_model)

    def test_save_creates_file(self):
        """Test save() creates a file"""
        self.storage.new(self.base_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_save_writes_json(self):
        """Test save() writes JSON to file"""
        self.storage.new(self.base_model)
        self.storage.save()
        with open(self.file_path, "r") as f:
            data = json.load(f)
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(key, data)
        self.assertEqual(data[key]["id"], self.base_model.id)
        self.assertEqual(data[key]["__class__"], "BaseModel")

    def test_reload_from_file(self):
        """Test reload() loads objects from file"""
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage.all().clear()
        self.storage.reload()
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, self.base_model.id)

    def test_reload_with_no_file(self):
        """Test reload() doesn't raise exception if file doesn't exist"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        try:
            self.storage.reload()
        except Exception as e:
            self.fail(f"reload() raised {e} unexpectedly!")

    def test_storage_with_different_classes(self):
        """Test storage with different class instances"""
        models = [
            User(),
            Place(),
            State(),
            City(),
            Amenity(),
            Review()
        ]
        
        for model in models:
            self.storage.new(model)
            key = "{}.{}".format(model.__class__.__name__, model.id)
            self.assertIn(key, self.storage.all())
            self.assertEqual(self.storage.all()[key], model)


if __name__ == "__main__":
    unittest.main()
