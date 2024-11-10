#!/usr/bin/python
""" holds class Amenity"""


import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Representation of Amenity, used same syntax in base_model"""
    if 'models' in globals() and models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
