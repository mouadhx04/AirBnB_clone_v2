#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
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
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """ Getter
        """
        pass
        # objects = storage.all(cities)
        # key = my_list[0] + '.' + my_list[1]
        # if key in objects:
        #     print(objects[key])
