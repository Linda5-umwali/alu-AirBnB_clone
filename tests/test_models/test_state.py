#!/usr/bin/python3
"""
Unittests for State class.
"""

import unittest
import os
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests for State class"""

    def setUp(self):
        """Set up for the tests"""
        self.state = State()

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_creation(self):
        """Test that a State instance is correctly created"""
        self.assertIsInstance(self.state, State)
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(self.state, BaseModel)
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_state_attributes(self):
        """Test that State has the required attributes"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_to_dict_method(self):
        """Test the to_dict method"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)

    def test_save_method(self):
        """Test that save method updates updated_at attribute"""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)
        self.assertGreater(self.state.updated_at, old_updated_at)

    def test_str_representation(self):
        """Test the __str__ method"""
        string = str(self.state)
        self.assertIn("[State]", string)
        self.assertIn(self.state.id, string)


if __name__ == "__main__":
    unittest.main()
