#!/usr/bin/python3
import unittest
from models import FileStorage, BaseModel, User


class TestFileStorage(unittest.TestCase):
    """Test class for FileStorage"""
    def test_new(self):
        """Test new method"""
        """Create a file storage object"""
        fs = FileStorage()
        """Create a base model object"""
        bm = BaseModel()
        """Call the new method with the base model object"""
        fs.new(bm)
        """Call the all method"""
        fs_all = fs.all()
        """Check if the object is stored in the __objects dictionary"""
        self.assertEqual(fs_all, fs.__objects)
        self.assertIn("BaseModel.{}".format(bm.id), fs_all)
        self.assertIs(fs_all["BaseModel.{}".format(bm.id)], bm)

    def test_new(self):
        """Test new method"""
        """Create a file storage object"""
        fs = FileStorage()
        """Create a user object"""
        user = User(email="bob@example.com", password="123456",
                    first_name="Bob", last_name="Smith")
        """Call the new method with the user object"""
        fs.new(user)
        """Check if the object is stored in the __objects dictionary"""
        self.assertIn("User.{}".format(user.id), fs.__objects)
        self.assertIs(fs.__objects["User.{}".format(user.id)], user)

    def test_save(self):
        """Test save method"""
        """Create a file storage object"""
        fs = FileStorage()
        """Create a base model object"""
        bm = BaseModel()
        """Call the new method with the base model object"""
        fs.new(bm)
        """Call the save method"""
        fs.save()
        """Check if the JSON file is created and has the correct content"""
        with open(fs.__file_path, "r") as f:
            content = f.read()
            self.assertIn("BaseModel.{}".format(bm.id), content)
            self.assertIn("\"__class__\": \"BaseModel\"", content)

    def test_reload(self):
        """Test reload method"""
        """Create a file storage object"""
        fs = FileStorage()
        """Create a user object"""
        user = User(email="bob@example.com", password="123456",
                    first_name="Bob", last_name="Smith")
        """Call the new method with the user object"""
        fs.new(user)
        """Call the save method"""
        fs.save()
        """Clear the __objects dictionary"""
        fs.__objects = {}
        """Call the reload method"""
        fs.reload()
        """Check if the object is restored in the __objects dictionary"""
        self.assertIn("User.{}".format(user.id), fs.__objects)
        self.assertIsInstance(fs.__objects["User.{}".format(user.id)], User)


if __name__ == '__main__':
    unittest.main()
