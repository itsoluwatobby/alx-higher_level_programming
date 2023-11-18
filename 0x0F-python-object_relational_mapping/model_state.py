#!/usr/bin/python3
"""
    Write a python file that contains the class definition of a
    State and an instance Base = declarative_base():
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    An instance of the state class
    Attributes:
        id(int): auto generated unique value, can't be null and
                is a primary key(pk)
        name(str): The name of the state, max 128 chars and can't
                be null
    """
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
