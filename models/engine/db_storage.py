#!/usr/bin/python3
'''
    Abstracted data storage
'''
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from model import classes


class DBStorage:
    """
        DBStroge abstract storage's engine for AirBnB program

    """
    __engine = None
    __session = None

    def __init__(self):
        '''
            Set the attributes of instantiate obj

            Args:
                No requirement arguemnt

            Attribures:
                No passed in value

            Return:
                None
        '''
        username = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database=os.getenv("HBNB_MYSQL_DB")

        connect_url = 'mysql+mysqldb://{}:{}@{}:3306/{}'.\
            format(username, passwd, host, database)

        self.__engine = create_engine(connect_url, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") is 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
            Fetch all stored data in storage

            Args:
                cls (class type): Filter key for stored data to retrieve

            Attributes:
                cls (key): Filter value

            Returns:
                collection of all classes or filtered obj
        '''
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if cls is not None:
            # collections = self.__session.query(cls).all()
            return collections
        else:
            # return self.__session.query
            pass
