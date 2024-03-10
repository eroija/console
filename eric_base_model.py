#!/usr/bin/python3
import unittest
from models import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel"""
    def test_init_with_kwargs(self):
        """Test __init__ with keyword arguments"""

        bm = BaseModel(id="123", created_at="2024-03-10T15:29:12.000000",
                       updated_at="2024-03-10T15:29:12.000000")

        """Check if the attributes are set correctly"""
        self.assertEqual(bm.id, "123")
        self.assertEqual(bm.created_at.isoformat(),
                         "2024-03-10T15:29:12.000000")
        self.assertEqual(bm.updated_at.isoformat(),
                         "2024-03-10T15:29:12.000000")

    def test_init_without_kwargs(self):
        """Test __init__ without keyword arguments"""
        """Create a base model object without keyword arguments"""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)
        self.assertEqual(bm.created_at, bm.updated_at)

    def test_save(self):
        """Test save method"""
        """Create a base model object"""
        bm = BaseModel()
        """Save the initial created_at and updated_at attributes"""
        old_created_at = bm.created_at
        old_updated_at = bm.updated_at
        """Call the save method"""
        self.assertNotEqual(bm.updated_at, old_updated_at)
        self.assertEqual(bm.created_at, old_created_at)

    def test_to_dict(self):
        """Test to_dict method"""
        bm = BaseModel()
        bm.name = "Alice"
        bm.age = 25
        """Call the to_dict method"""
        self.assertEqual(bm_dict["id"], bm.id)
        self.assertEqual(bm_dict["name"], "Alice")
        self.assertEqual(bm_dict["age"], 25)
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        """Check if the dictionary has only the expected keys"""
        self.assertEqual(len(bm_dict), 6)
        self.assertIn("id", bm_dict)
        self.assertIn("name", bm_dict)
        self.assertIn("age", bm_dict)
        self.assertIn("created_at", bm_dict)
        self.assertIn("updated_at", bm_dict)
        self.assertIn("__class__", bm_dict)e

    def test_str(self):
        """Test __str__ method"""
        """Create a base model object with some attributes"""
        bm = BaseModel()
        bm.name = "Bob"
        bm.age = 30
        """Call the __str__ method"""
        bm_str = str(bm)
        """Check if the string has the correct format"""
        self.assertEqual(bm_str[:9], "[BaseModel]")
        self.assertEqual(bm_str[10:46], "({})".format(bm.id))
        self.assertIn("'name': 'Bob'", bm_str)
        self.assertIn("'age': 30", bm_str)
        self.assertIn("'created_at':", bm_str)
        self.assertIn("'updated_at':", bm_str)


if __name__ == '__main__':
    unittest.main()
