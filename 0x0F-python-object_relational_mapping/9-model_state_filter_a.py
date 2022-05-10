#!/usr/bin/python3
"""
    List all object of a tables(class)
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    data = session.query(State).filter(
        State.name.contains("a")).order_by(
        State.id)
    if data is None:
        print("Nothing")
    else:
        for state in data:
            print("{}: {}".format(state.id, state.name))

    session.close()
