#!/usr/bin/python3
"""
Create a model City with sqlalchemy
"""

from sqlalchemy import Column, Integer, String, ForeignKeyConstraint
from relationship_state import Base


class City(Base):
    """
    Model State inherit from Base
    """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(['state_id'], ['states.id']),
    )
