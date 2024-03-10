#!/usr/bin/python3
import unittest
from models import User


class TestUser(unittest.TestCase):
    """Test class for User"""
    def test_init(self):
        """Create a user object with some attributes"""
        user = User(email="alice@example.com", password="123456",
                    first_name="Alice", last_name="Smith")
        """Check if the attributes are set correctly"""
        self.assertEqual(user.email, "alice@example.com")
        self.assertEqual(user.password, "123456")
        self.assertEqual(user.first_name, "Alice")
        self.assertEqual(user.last_name, "Smith")
        """ Check if the user object inherits from BaseModel"""
        self.assertIsInstance(user, BaseModel)

    def test_validation(self):
        """Test data validation"""
        """Create a user object with invalid email"""
        with self.assertRaises(ValueError):
            user = User(email="invalid", password="123456",
                        first_name="Alice", last_name="Smith")
        """Create a user object with invalid password"""
        with self.assertRaises(ValueError):
            user = User(email="alice@example.com", password="",
                        first_name="Alice", last_name="Smith")
        """Create a user object with invalid first name"""
        with self.assertRaises(ValueError):
            user = User(email="alice@example.com", password="123456",
                        first_name=123, last_name="Smith")
        """Create a user object with invalid last name"""
        with self.assertRaises(ValueError):
            user = User(email="alice@example.com", password="123456",
                        first_name="Alice", last_name=456)


if __name__ == '__main__':
    unittest.main()
