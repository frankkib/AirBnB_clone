#!/usr/bin/python3
"""class amenity module"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """class representation"""
    def test_amenity(self):
        """the tests"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        """tests for inhertance"""
        self.assertTrue(issubclass(Place, BaseMode))


if __name__ == "__name__":
    unittest.main()
