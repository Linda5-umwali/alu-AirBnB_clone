#!/usr/bin/python3
"""
Unittests for City class.
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for City"""

    def test_instance_creation(self):
        """Test that an instance is correctly created"""
        city = City()
        self.assertIsInstance(city, City)


if __name__ == "__main__":
    unittest.main()
