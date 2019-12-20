#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        __tablename__: SQL table
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    # place_amenities = ""
