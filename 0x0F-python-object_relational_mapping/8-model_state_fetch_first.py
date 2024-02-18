#!/usr/bin/python3

"""
prints the first State object from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:
    {password}@localhost/{db}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    
    if first_state:
        print(f"{State.id}: {State.name}")
    else:
        print("Nothing")

    session.close()
