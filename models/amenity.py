#!/usr/bin/python
""" holds class Amenity"""

from models.place import place_amenity
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of Amenity, used same syntax in base_model"""
    
    __tablename__ = "amenities"

    if BaseModel.storage_type == "db":
        name = Column(String(128), nullable=False)

        place_amenities = relationship(
            "Place", secondary=place_amenity,
            back_populates="amenities",
            viewonly=False)
    else:
        name = ""
        
    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
