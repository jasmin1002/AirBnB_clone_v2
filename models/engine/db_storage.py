#!/usr/bin/python3
'''
    Abstracted data storage
'''
import os
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
#from models.place import Place
from models.review import Review
from models.amenity import Amenity


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
        database = os.getenv("HBNB_MYSQL_DB")

        # Database connection url
        connect_url = 'mysql+mysqldb://{}:{}@{}:3306/{}'.\
            format(username, passwd, host, database)

        # Create lazy database connection
        self.__engine = create_engine(connect_url, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == 'test':
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
        collection = {}

        if cls is not None:
            queryset = self.__session.query(cls).all()
            for obj in queryset:
                key = type(obj).__name__ + '.' + obj.id
                collection[key] = obj

            return collections

        else:
            # Supported classes/tables for Airbnb app
            classes = [
                City,
                State,
                User,
                Review,
                Amenity
            ]
            tmp = []

            for cls in classes:
                queryset = self.__session.query(cls).all()
                tmp.extend(queryset)

            for obj in tmp:
                key = type(obj).__name__ + '.' + obj.id
                collection[key] = obj
            return collection

    def new(self, obj):
        self.__session.add(obj)
        self.save()

    def save(self):
        self.__session.commit()
        self.__session.close()

    def delete(self, obj=None):
        pass

    def reload(self):
        # Create all required and neccessary tables
        try:
            Base.metadata.create_all(self.__engine)

            # Establish connection for transaction
            session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
            Session = scoped_session(session_factory)
            self.__session = Session()
        except exc.OperationalError as err:
            msg = "Operation error: cant't connect. Ensure database server\
 is start and running."
            print("{}".format(msg))
        except Exception as err:
            print("Error: {}".format(type(err)))
