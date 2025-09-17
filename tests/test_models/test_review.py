#!/usr/bin/python3
"""
Unittests for Review class.
"""

import unittest
import os
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests for Review class"""

    def setUp(self):
        """Set up for the tests"""
        self.review = Review()

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_creation(self):
        """Test that a Review instance is correctly created"""
        self.assertIsInstance(self.review, Review)
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(self.review, BaseModel)
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_review_attributes(self):
        """Test that Review has the required attributes"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_to_dict_method(self):
        """Test the to_dict method"""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)

    def test_save_method(self):
        """Test that save method updates updated_at attribute"""
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)
        self.assertGreater(self.review.updated_at, old_updated_at)

    def test_str_representation(self):
        """Test the __str__ method"""
        string = str(self.review)
        self.assertIn("[Review]", string)
        self.assertIn(self.review.id, string)


if __name__ == "__main__":
    unittest.main()
