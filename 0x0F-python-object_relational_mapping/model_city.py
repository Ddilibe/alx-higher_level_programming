#!/usr/bin/python3
"""
    Script containing the model class definition for a city
"""

from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    Model class that contains a definition of a city
    It inherits the Base declarative class
    @args:
        id: Represents a column of an auto generated unique integer
        name: column of string of 128 characters
        state_id: Represents the foreign key to the state.id
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    def __repr__(self):
        """Method used for describing the class"""
        return "City<id='{}', name='{}', state='{}'>".format(
            self.id, self.name, self.state_id
        )
