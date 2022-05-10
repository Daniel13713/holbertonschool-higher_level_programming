#!/usr/bin/python3
"""
    List all object of a tables(class)
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, desc
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
        """Insert data"""
        new_data = State(
            name="Louisiana"
        )
        session.add(new_data)
        session.commit()

        """Fetch all data"""
        data = session.query(State).order_by(
            desc(State.id)).first()

    if not data:
        print("Nothing")
    else:
        print("{}".format(data.id))
