#!/usr/bin/python3
# Creates the State “California” with the City “San Francisco”
# from the database hbtn_0e_100_usa.
# Usage: ./100-relationship_states_cities.py <mysql username> /
#                                            <mysql password> /
#                                            <database name>
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, passwd, db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    newState = City(name="San Francisco", state=State(name="California"))
    session.add(newState)
    session.commit()

    session.close()