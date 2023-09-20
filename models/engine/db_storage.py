#!/usr/bin/python3
''' DATABASE storage class
*****
'''
from models import stringtemplates as ENV
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine, MetaData
from models.city import City
import models


class DBStorage:
    ''' ***Create SQLAlchemy** DATABASE**
    *****
    '''
    __engine = None
    __session = None

    def __init__(self) -> None:
        ''' ***Create engine and link to MySQL databse Class constructor**
        *****
        '''

        user = getenv(ENV.HBNB_MYSQL_USER)
        pwd = getenv(ENV.HBNB_MYSQL_PWD)
        host = getenv(ENV.HBNB_MYSQL_HOST)
        db = getenv(ENV.HBNB_MYSQL_DB)
        env = getenv(ENV.HBNB_ENV, 'none')

        self.__engine = create_engine(connection, pool_pre_ping=True)
        connection = f'mysql+mysqldb://{user:s}:{pwd:s}@{host:s}/{db:s}'

        if env == ENV.TEST:
            Base.metadata.drop_all(self.__engine)

    def reload(self) -> None:

        '''*** Current DATABASE changes and session to be Commited**
        *****
        '''
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def all(self, cls=None) -> dict:
        ''' ***Query current DB session or Specific one**
        *****
        '''
        database = {}

        if cls != '':
            objs = self.__session.query(models.classes[cls]).all()
            for obj in objs:
                key = f'{obj.__class__.__name__}.{obj.id}'
                database[key] = obj
            return database
        else:
            for key, value in models.classes.items():
                if key != 'BaseModel':
                    objs = self.__session.query(value).all()
                    if len(objs):
                        for obj in objs:
                            k = f'{obj.__class__.__name__}.{obj.id}'
                            database[k] = obj
            return database

    def new(self, obj) -> None:
        '''***Add object to DATABASE***
        *****
        '''
        self.__session.add(obj)

    def save(self):
        '''***Commit all current DATABAASE changes**
        *****
        '''
        self.__session.commit()

    def delete(self, obj=None) -> None:
        '''***Delete current DATABASE session**
        *****
        '''
        if obj is None:
            return
        self.__session.delete(obj)

    def close(self) -> None:
        '''***Private session attribute Must be removed**
        *****
        '''
        self.__session.close()
