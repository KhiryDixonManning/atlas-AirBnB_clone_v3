#!/usr/bin/python3
"""
storage_t defined
"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
