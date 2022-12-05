#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """returns the list of City instances with state_id equals
         to the current State.id"""
        from models import storage, storage_env
        from models.city import City

        if storage_env == 'db':
            return State.cities
        else:
            all_cities = storage.all(City)
            cities = []

            for city in all_cities.values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities


State.cities = relationship("City", back_populates="state",
                            cascade="all,delete, delete-orphan")
