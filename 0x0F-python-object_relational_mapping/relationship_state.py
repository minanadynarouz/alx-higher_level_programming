#!/usr/bin/python3

"""
class definition of a State and an instance Base = declarative_base()
"""

import MySQLdb
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

Base = declarative_base()


class State(Base):
    """Table Declaration"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
