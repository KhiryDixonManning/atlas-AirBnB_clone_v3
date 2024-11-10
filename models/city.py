#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

# Base = decalarative_base()


class City(BaseModel, Base):
    """
    Rep of city
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities")

    def __init__(self, *args, **kwargs):
        """
        initializes city
        """
        super().__init__(*args, **kwargs)
        if models.storage_t != "db":
            self.state_id = ""
            self.name = ""
