#!/usr/bin/python3
"""
Unittests for BaseModel class.
"""

import unittest
import uuid
from datetime import datetime
import json
import os
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def setUp(self):
        """Set up for the tests"""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_creation(self):
        """Test that an instance is correctly created"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """Test the __str__ method"""
        string = str(self.model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(self.model.id, string)

    def test_save_method(self):
        """Test the save method"""
        original_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_updated_at, self.model.updated_at)
        self.assertGreater(self.model.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_init_with_kwargs(self):
        """Test initialization with kwargs"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertIsNot(self.model, new_model)

    def test_init_without_kwargs(self):
        """Test initialization without kwargs"""
        new_model = BaseModel()
        self.assertNotEqual(self.model.id, new_model.id)
        self.assertNotEqual(self.model.created_at, new_model.created_at)
        self.assertNotEqual(self.model.updated_at, new_model.updated_at)


if __name__ == "__main__":
    unittest.main()
