#!/usr/bin/python3
"""
Unittests for City class.
"""

import unittest
import os
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests for City class"""

    def setUp(self):
        """Set up for the tests"""
        self.city = City()

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_creation(self):
        """Test that a City instance is correctly created"""
        self.assertIsInstance(self.city, City)
        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(self.city, BaseModel)
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_city_attributes(self):
        """Test that City has the required attributes"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_to_dict_method(self):
        """Test the to_dict method"""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)

    def test_save_method(self):
        """Test that save method updates updated_at attribute"""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)
        self.assertGreater(self.city.updated_at, old_updated_at)

    def test_str_representation(self):
        """Test the __str__ method"""
        string = str(self.city)
        self.assertIn("[City]", string)
        self.assertIn(self.city.id, string)


if __name__ == "__main__":
    unittest.main()
