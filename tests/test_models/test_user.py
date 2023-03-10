#!/usr/bin/python3
import unittest
from models.user import User

"""class user test module"""


class TestUser(unittest.TestCase):
    """class represenation"""
    def test_attributes(self):
        """testing the user attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        """tests for inhertance"""
        self.assertTrue(issubclass(Place, BaseMode))


if __name__ == "__main__":
    main()
