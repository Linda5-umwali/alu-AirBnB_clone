#!/usr/bin/python3
"""
Unittests for State class.
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests for State"""

    def test_instance_creation(self):
        """Test that an instance is correctly created"""
        state = State()
        self.assertIsInstance(state, State)


if __name__ == "__main__":
    unittest.main()
