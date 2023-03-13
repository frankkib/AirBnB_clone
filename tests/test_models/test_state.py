#!/usr/bin/python3
"""class test state mdoule"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """class representation"""
    def test_state(self):
        """tests"""
        state = State()
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        """tests for inhertance"""
        state = State()
        self.assertTrue(issubclass(state, BaseMode))


if __name__ == "__main__":
    unittest.main()
