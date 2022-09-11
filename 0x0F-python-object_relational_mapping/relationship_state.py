#!/usr/bin/python3
"""
    Module containing the class definition of State
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()
class State(Base):
    """
        Class blueprint for the class definition of State
        @args:
            id: represents a column of auto-generated, unique Integers
            name: represents a column of string with maximum 128 character
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states')

    def __repr__(self):
        """ Method used for describing the class """
        return "User<id='{}', name='{}'>".format(self.id, self.name)
