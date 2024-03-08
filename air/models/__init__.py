#!/usr/bin/python3
"""
The module acts as an initialization file
for the modules package
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
