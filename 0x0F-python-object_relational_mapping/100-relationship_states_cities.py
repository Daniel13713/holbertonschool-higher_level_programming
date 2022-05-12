#!/usr/bin/python3
"""
    List all object of a tables(class)
"""
import sys
from relationship_state import Base, State
from relationship_city import City
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
        """Insert state"""
        new_state = State(
            name="California"
        )
        """Insert new City with state id created"""
        new_city = City(
                name="San Francisco"
            )
        new_state.cities = [
            new_city
        ]
        session.add(new_state)
        session.commit()

        session.close()
