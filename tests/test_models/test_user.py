#!/usr/bin/python3
"""
Unittests for User class.
"""

import unittest
import os
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests for User class"""

    def setUp(self):
        """Set up for the tests"""
        self.user = User()

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_creation(self):
        """Test that a User instance is correctly created"""
        self.assertIsInstance(self.user, User)
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_user_attributes(self):
        """Test that User has the required attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict_method(self):
        """Test the to_dict method"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

    def test_save_method(self):
        """Test that save method updates updated_at attribute"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)
        self.assertGreater(self.user.updated_at, old_updated_at)

    def test_str_representation(self):
        """Test the __str__ method"""
        string = str(self.user)
        self.assertIn("[User]", string)
        self.assertIn(self.user.id, string)


if __name__ == "__main__":
    unittest.main()
