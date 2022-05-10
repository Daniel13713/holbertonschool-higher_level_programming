#!/usr/bin/python3
"""
    List a states table
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """
        Don't execute when is imported
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    query = "SELECT * FROM states ORDER BY states.id"
    data = engine.execute(query)
    for state in data:
        print("{}: {}".format(state.id, state.name))
