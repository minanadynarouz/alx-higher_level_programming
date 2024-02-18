#!/usr/bin/python3

"""
lists all State objects that contain the letter a from database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmakder
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}')
    base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    withLetter = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

    for state in withLetter:
        print(f'{State.id}: {State.name}')

    session.close()
