#!/usr/bin/python3
"""This defines the FileStorage class."""
import json


class FileStorage:
    """
    file storage system for storing and retrieving
    objects.
    """
    def __init__(self):
        """
        Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
        """

        __file_path = "file.json"
        __objects = {}

    def all(self):
        """Returns the dictionary of stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets an object in __objects with key
        <obj class name>.id.
        """
        key = "{} {]".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dumps(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as file:
                serialized = json.load(file)

            for key, value in serialized.items():
                self.__objects[key] = eval(
                     f"{value['__class__']}(**{value})")

        except FileNotFoundError:
            return
