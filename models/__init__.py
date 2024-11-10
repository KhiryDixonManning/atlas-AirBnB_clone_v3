#!/usr/bin/python3
"""
storage_t defined
"""
import os

storage_t = os.environ.get('HBNB_TYPE_STORAGE', 'file')
db = os.environ.get('HBNB_ENV', 'test')

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
