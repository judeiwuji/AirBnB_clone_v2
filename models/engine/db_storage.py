#!/usr/bin/python3
"""This module contains DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """DBStorage - provides an interface between the DB and APP"""

    __engine = None
    __session= None

    def __init__(self):
        """Creates DBStorage instance"""
        DB_USER = getenv('HBNB_MYSQL_USER')
        DB_PASS = getenv('HBNB_MYSQL_PWD')
        DB_HOST = getenv('HBNB_MYSQL_HOST')
        DB_NAME = getenv('HBNB_MYSQL_DB')
        DB_URL = "mysql+mysqldb://{}:{}@{}/{}".\
                                      format(DB_USER, DB_PASS, DB_HOST, DB_NAME)

        self.__engine = create_engine(DB_URL, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            pass

    def all(self, cls=None):
        """query on the current database session
        Args:
            cls(str): The class to be returned
        """
        objects = {}
        data = []
        if cls is not None:
            data = self.__session(cls).all()
        else:
            from models.city import City
            from models.state import State
            # from models.amenity import Amenity
            # from models.place import Place
            # from models.review import Review
            # from models.user import User
            entities = [ State, City] # Amenity, Place, Review, User]

            for entity in entities:
                data[len(data):] = self.__session(entity).all()
        for obj in data:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objects[key] = obj
        return objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads all entity objects"""
        from models.base_model import Base
        from models.state import State
        from models.city import City

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
