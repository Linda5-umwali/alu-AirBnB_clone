#!/usr/bin/python3
"""
Unittests for Review class.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for Review"""

    def test_instance_creation(self):
        """Test that an instance is correctly created"""
        review = Review()
        self.assertIsInstance(review, Review)


if __name__ == "__main__":
    unittest.main()
