#!/usr/bin/python3
"""
Unittests for FileStorage engine.
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage"""

    def test_all_return_type(self):
        """Test all() returns a dictionary"""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new_creates_key(self):
        """Test new() adds an object"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage.all())

if __name__ == "__main__":
    unittest.main()
