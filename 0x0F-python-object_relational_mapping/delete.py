#!/usr/bin/python3
"""
    Deleting a data
"""
import sys
from relationship_state import Base, State
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
        """Deleting data"""

        try:
            """Fetch and delete data with pattern"""
            data = session.query(State).get(1)
            session.delete(data)
            session.commit()
        except Exception as err:
            print("Fetch:\n", err)
