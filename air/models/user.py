#!/usr/bin/python3
"""This defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class representing user data.
    Attributes:
        email (str): User's email address (default is an empty string).
        password (str): User's password (default is an empty string).
        first_name (str): User's first name (default is an empty string).
        last_name (str): User's last name (default is an empty string).
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
