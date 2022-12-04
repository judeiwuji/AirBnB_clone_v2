#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all,delete, delete-orphan")

    @property
    def cities(self):
        """returns the list of City instances with state_id equals
        to the current State.id"""
        from models import storage
        from models.city import City

        all_cities = storage.all(City)
        cities = []

        for city in all_cities.values():
            if city.state_id == self.id:
                cities.append(city)
        return cities;
