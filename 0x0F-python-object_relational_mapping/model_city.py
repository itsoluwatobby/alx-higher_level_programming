#!/usr/bin/python3
"""
    Write a python file that contains the class definition of a 
    City and an instance Base = declarative_base():
"""
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base


class City(Base):
    """
    An instance of the city class
    Attributes:
        id(int): auto generated unique value, can't be null and
            is a primary key(pk)
        name(str): The name of the city, max 128 chars and can't be null
        state_id(int): id from the state model and can't be null
    """
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
