#!/usr/bin/python3
"""
Unittests for Place class.
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for Place"""

    def test_instance_creation(self):
        """Test that an instance is correctly created"""
        place = Place()
        self.assertIsInstance(place, Place)


if __name__ == "__main__":
    unittest.main()
