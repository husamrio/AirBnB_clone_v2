#!/usr/bin/python3
""" State Module for HBNB project
*****
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
from models.place import place_amenity
from models.stringtemplates import HBNB_TYPE_STORAGE, DB


class Amenity(BaseModel, Base):
    """***This is class for Amenity
    Attributes**:
        name: input name
    """
    __tablename__ = "amenities"
    if getenv(HBNB_TYPE_STORAGE) == DB:
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",
                                       secondary=place_amenity,
                                       back_populates='amenities')
    else:
        name = ""
