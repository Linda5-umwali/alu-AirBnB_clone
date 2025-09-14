#!/usr/bin/python3
"""
Unittests for BaseModel class.
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel"""

    def test_instance_creation(self):
        """Test that an instance is correctly created"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))


if __name__ == "__main__":
    unittest.main()
