#!/usr/bin/python3
"""class review module"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """class review representattion"""
    def test_review(self):
        """class review tests"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_inheritance(self):
        """tests for inhertance"""
        self.assertTrue(issubclass(Place, BaseMode))


if __name__ == "__main__":
    unittest.main()
