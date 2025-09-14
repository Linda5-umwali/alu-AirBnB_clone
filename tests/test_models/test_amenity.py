#!/usr/bin/python3
"""
Unittests for Amenity class.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for Amenity"""

    def test_instance_creation(self):
        """Test that an instance is correctly created"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)


if __name__ == "__main__":
    unittest.main()
