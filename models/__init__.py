#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


storage_type = os.getenv("HBNB_TYPE_STORAGE")
print(storage_type)
storage = ''

if storage_type is 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
# storage = FileStorage()

storage.reload()
