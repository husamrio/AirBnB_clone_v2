#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City

if getenv(HBNB_TYPE_STORAGE) == DB:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

classes = {'User': User, 'BaseModel': BaseModel,
           'Place': Place, 'State': State, 'City': City,
           'Amenity': Amenity, 'Review': Review}

storage.reload()
