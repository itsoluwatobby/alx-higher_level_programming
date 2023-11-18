#!/usr/bin/python3
"""Write a python file that contains the class definition of a
    State and an instance Base = declarative_base()
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """
    An instance of the state class
    Attributes:
        id(int): auto generated unique value, can't be null
                and is a primary key(pk)
        name(str): The name of the state, max 128 chars and
                can't be null
        cities (sqlalchemy.orm.relationship): The State-City
                relationship.
    """
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship(
            'City', backref="state", cascade="all, delete")
