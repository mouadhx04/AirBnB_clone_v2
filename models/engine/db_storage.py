#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""

from models.base_model import BaseModel
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


# Note: remember to update __init__.py as per task 6 as well

class DBStorage:
    """This class handles the MySQL database engine
    Attributes:
        __engine: initially set to None, becomes sqlalchemy engine
        __session: initially set to None, becomes sqlalchemy session
    """

    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of DBStorage class
        Attributes:
        engine: links to MySQL database using environment variables
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all()

    def all(self, cls=None):
        """ Queries current database session for class objects
        If class not specified, queries all types of objects
        """
        return_dic = {}
        if cls:
            query = self.__session.query(cls.__name__).all()
            for obj in query:
                if "_sa_instance_state" in type(obj).__name__:
                    continue
                key = "{}.{}".format(type(obj).__name__, obj.id)
                return_dic[key] = obj
            return return_dic
        else:
            query = self.__session.query(City).all()
            query.append(self.__session.query(State).all())
            for obj in query:
                if "_sa_instance_state" in type(obj).__name:
                    continue
                key = "{}.{}".format(type(obj).__name__, obj.id)
                return_dic[key] = obj
            return return_dic

    def new(self, obj):
        """add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """ commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database
        creates the current database session (self.__session)
        from the engine (self.__engine)
        """
        Base.metadata.create_all(self.__engine)
        session_make = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session_scoped = scoped_session(session_make)
        self.__session = session_scoped()
