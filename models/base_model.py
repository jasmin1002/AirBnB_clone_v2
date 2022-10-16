#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model

            Args:
                *args: Variable length argument list
                **kwargs: Arbitrary keyword arguments.
        """
        if 'id' not in kwargs:
            #: str: unique identity attached to an instance obj
            self.id = str(uuid4())

            #: datetime: updated_at set to datetime obj
            self.updated_at = datetime.now()

            #: datetime: created_at set to datetime obj
            self.created_at = datetime.now()

            #: str: name of an instance obj
            if 'name' in kwargs:
                self.name = kwargs['name']

        else:
            for (key, value) in kwargs.items():
                if isinstance(key, datetime):

                    #: str: created_at or updated_at convert to datetime str
                    self[key] = datetime.strptime(
                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f'
                    )
                elif key != '__class__':
                    #: str: every other attributes except one with __class__
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
            type(self).__name__,
            self.id,
            self.to_dict()
        )

    def save(self):
        from models import storage
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert class instance into dict representation

            Args:
                No required parameter

            Returns:
                dict if successful, like:
                {
                    'id': 'e792-3f34-233-0032f',
                    'created_at': '2022-08-07T21:05:54.1195572',
                    'updated_at': '2022-08-07T21:05:54.1192411',
                    '__class__': 'BaseModel'
                }

            Raises:
                keyError: dict does not have to_dict

        """
        new_dict = {}
        for (key, value) in self.__dict__.items():
            if type(value) is datetime:
                new_dict[key] = value.isoformat()
            elif key == '_sa_instance_state':
                continue
            else:
                new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def delete(self):
        '''
        Remove an instance object from data set

        Args:
            No required parameter

        Returns:
            Always return None
        '''
        storage.delete(self)
