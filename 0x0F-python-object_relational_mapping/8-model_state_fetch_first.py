#!/usr/bin/python3
"""script to print state object"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    userName = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        userName, password, db))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if not state:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()
