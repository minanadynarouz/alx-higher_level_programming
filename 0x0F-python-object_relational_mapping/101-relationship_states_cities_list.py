#!/usr/bin/python3
"""Lists all State objects and corresponding City"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    """
    Script to print states and cities
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
