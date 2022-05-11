#!/usr/bin/python3
"""
Create a model City with sqlalchemy
"""

from sqlalchemy import (Column,
                        Integer,
                        String,
                        ForeignKeyConstraint,
                        ForeignKey
                        )
from relationship_state import Base, State
from sqlalchemy.orm import relationship


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
    state_id = Column(
        Integer,
        ForeignKey(
            'states.id',
            ondelete='CASCADE'),
        nullable=False)

    state = relationship(
        'State', backref=backref(
            'cities', passive_deletes=True))
