#!/usr/bin/python3
"""class place module"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """class place representation"""
    def test_place(self):
        """class palce tests"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
        
        def test_inheritance(self):
            """tests for inhertance"""
            place = Place()
            self.assertTrue(issubclass(Place, BaseMode))


if __name__ == "__main__":
    unittest.main()
