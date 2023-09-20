#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from models.state import State
from models.stringtemplates import HBNB_TYPE_STORAGE, DB


class City(BaseModel):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'
    if (getenv(HBNB_TYPE_STORAGE) == DB):

        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

        name = Column(String(128), nullable=False)

        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        state_id = ""
        name = ""
