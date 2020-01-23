#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
import models
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

"""
# TO DO:
# cities getter
#for FileStorage: getter attribute cities that returns
#the list of City instances with state_id equals to the
#current State.id =>
#It will be the FileStorage relationship between State and City
"""


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    __tablename__: SQL table
    cities: for DBStorage, creates relationship for class City to state table
    """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """ Getter
            """
            r_v = []
            objs = storage.all()
            for key in objs.keys():
                if key.split(".")[0] == "City":
                    if key.split(".")[1] == self.id:
                        r_v.append(objs[key])
            return (r_v)
