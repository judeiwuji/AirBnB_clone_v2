#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = "cities"

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        state = relationship("State", back_populates="cities")
        places = relationship("Place", back_populates="cities",
                              cascade="all, delete, delete-orphan")
else:
    class City(BaseModel):
        """ The city class, contains state ID and name """
        name = ""
        state_id = ""
