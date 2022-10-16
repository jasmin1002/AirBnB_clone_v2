#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship(
        'City',
        cascade='all, delete, delete-orphan',
        back_populates='state'
    )

    @property
    def cities(self):
        from models import storage
        from models.city import City

        #: list of city: Stores list of city of current state
        city_list = []

        # Retrieve all city instances in storage
        all_cities = storage.all(City).values()

        # For each iteration through all_cities list,
        # retrieve city associate with current state
        # i.e where city's state_id equals state's id
        for city in all_cities:
            if city.state_id == self.id:
                city_list.append(city)

        return city_list
