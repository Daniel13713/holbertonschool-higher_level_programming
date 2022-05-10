#!/usr/bin/python3
"""
    List all object of a tables(class)
"""
import sys
from model_city import Base, City
from model_state import State
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

    with Session(engine) as session:
        data = session.query(
            City,
            State).filter(
            State.id == City.state_id).order_by(
            City.id).all()
        for city, state in data:
            print("{0}: ({1}) {2}".format(state.name, city.id, city.name))
