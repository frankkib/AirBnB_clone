#!/usr/bin/python3
"""class city module"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """class representation"""
    def test_city(self):
        """test"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_inheritance(self):
        """tests for inhertance"""
        self.assertTrue(issubclass(Place, BaseMode))


if __name__ == "__main__":
    unittest.main()
