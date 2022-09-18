#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # Relationships
    cities = relationship('City')
    user = relationship('User')
    reviews = relationship(
        'Review',
        cascade='all, delete, delete-orphan',
        back_populates='place'
    )

    amenities = relationship(
        'Amenity',
        secondary=place_amenity,
        viewonly=False
    )

    #places = relationship('Place')

    @property
    def reviews(self):
        return reviews  # Incomplete to work with FileStorage (Modify later)

    @property
    def amenities(self):
        return amenities    # Incomplete code for FileStorage (Modify later)

    @amenities.setter
    def amenities(self, id):
        pass    # Incomplete code for FileStorage (Modify later)
