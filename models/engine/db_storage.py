#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""
import os
import json
from models.base_model import BaseModel
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


# TO DO:
# In __init__ method: Environment variables for self.__engine
# Code all task requirements for:
# all method (self.__session called in reload)
# new method (add object to self.__session)
# save method (commit changes of self.__session)
# delete method (delete obj from self.__session)
# reload method (creates tables, has sessionmaker using scoped_session
# Note: remember to update __init__.py as per task 6 as well

class DBStorage:
    """This class handles the MySQL database engine
    Attributes:
        __engine: set to None (task 6)
        __session: set to None (task 6)
    """

    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of DBStorage class
        Attributes:
        engine: links to MySQL database using environment variables
        """
        self.__engine = create_engine('mysql+mysqldb://{USERNAME}:{PASSWORD}@
        {HOST}/{DATABASE}', pool_pre_ping=True)
        # drop all tables if the environment variable HBNB_ENV is equal to test

    def all(self, cls=None):
        """ Queries current database session for class objects
        If class not specified, queries all types of objects
        """
        pass
        # classes = {"Amenity": Amenity,
        #            "City": City,
        #            "Place": Place,
        #            "Review": Review,
        #            "State": State,
        #            "User": User}

        # query on the current database session (self.__session) all objects depending of the class name (argument cls)
        # if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
        # this method must return a dictionary: (like FileStorage)
        # key = <class-name>.<object-id>
        # value = object

    def new(self, obj):
        """add the object to the current database session
        """
        pass

    def save(self):
        """ commits all changes of the current database session
        """
        pass

    def delete(self, obj=None):
        """ deletes from the current database session obj if not None
        """
        pass

    def reload(self):
        """creates all tables in the database
        creates the current database session (self.__session)
        from the engine (self.__engine)
        """
        pass
        # create the current database session (self.__session) from the engine (self.__engine) by using a sessionmaker - the option expire_on_commit must be set to False ; and scoped_session - to make sure your Session is thread-safe
