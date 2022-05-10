#!/usr/bin/python3
"""
    Updating a data
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
        """updating data"""

        try:
            """Fetch data with id=2"""
            data = session.query(State).filter(State.id == 2).first()
        except Exception as err:
            print("Fetch:\n", err)
        try:
            """Change data (name)"""
            data.name = "New Mexico"

            """Save the data changed"""
            session.add(data)
            session.commit()
        except Exception as err:
            print("Save:\n", err)
