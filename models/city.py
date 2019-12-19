#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
        __tablename__: SQL table
    """
    state_id = Column(String(60), nullable=False, ForeignKey('states.id')
    name = Column(String(128), nullable=False)
    __tablename__ = 'cities'
