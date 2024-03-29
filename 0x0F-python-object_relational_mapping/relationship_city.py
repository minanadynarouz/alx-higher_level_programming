#!/usr/bin/python3

"""
class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id (sqlalchemy.Column): The city's id.
        name (sqlalchemy.Column): The city's name.
        state_id (sqlalchemy.Column): The city's state id.
    """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=False)
    name = Column(
        String(128),
        nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False)
