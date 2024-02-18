#!/usr/bin/python3

"""
class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Table Declaration"""
    __tablename__ = 'cities'
    id = Column(
            Interger,
            unique=True,
            autoincrement=True,
            nullable=False,
            primary_key=True)
    name = Column(
            String(128),
            nullable=False)
    state_id = Column(
            Integer,
            nullable=False,
            ForeignKey('states.id'))
    state = relationship('State')
