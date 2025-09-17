#!/usr/bin/python3
"""
Unittests for Amenity class.
"""

import unittest
import os
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Tests for Amenity class"""

    def setUp(self):
        """Set up for the tests"""
        self.amenity = Amenity()

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_creation(self):
        """Test that an Amenity instance is correctly created"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_amenity_attributes(self):
        """Test that Amenity has the required attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_to_dict_method(self):
        """Test the to_dict method"""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)

    def test_save_method(self):
        """Test that save method updates updated_at attribute"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)
        self.assertGreater(self.amenity.updated_at, old_updated_at)

    def test_str_representation(self):
        """Test the __str__ method"""
        string = str(self.amenity)
        self.assertIn("[Amenity]", string)
        self.assertIn(self.amenity.id, string)


if __name__ == "__main__":
    unittest.main()
