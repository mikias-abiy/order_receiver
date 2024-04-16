#!/usr/bin/python3


"""
db_storage.py:
    This module holds the defination of the class DBStorage
    which handles the storage of objects in database using
    storm ORM.
"""


from dotenv import dotenv_values

from storm.locals import Store, create_database

from config import F_ENV

class DBStorage:
    """
    DBStorage:
        handles object storage in database using storm ORM.
    """
    __store = None

    def __init__(self):
        env_vars = dotenv_values(F_ENV)

        user = env_vars['BOT_MYSQL_USER']
        passwd = env_vars['BOT_MYSQL_PWD']
        host = env_vars['BOT_MYSQL_HOST']
        db_name = env_vars['BOT_MYSQL_DB']

        # MySQL database uri.
        db_url = f'mysql://{user}:{passwd}@{host}/{db_name}'
        
        # sqlite database uri.
        # db_url = f'sqlite:{db_name}.db'

        self.database = create_database(db_url)
        self.__store = Store(database=self.database)
    
    @property
    def store(self):
        return self.__store
    
    def connect(self):
        db = self.__store.get_database()
        db.connect()

    def new(self, obj):
        """
        new:
            Inserts new object to the collection of objects.

        Args:
            obj: The object to be stored.

        Return:
            None.
        """
        self.connect
        self.__store.add(obj)
        self.save()

    def remove(self, obj):
        """
        remove:
            Removes an object from the collection of objects.

        Args:
            obj: The object to be stored.

        Return:
            None.
        """
        self.connect
        self.__store.remove(obj)
        self.save()

    def save(self):
        """
        save(self):
            Saves the objects collection dictionary in to a file
            after converting it to a json representation.

        Return:
            None.
        """
        self.__store.flush()
        self.__store.commit()
    
    def get(self, cls):
        self.connect()
        from models.db_models.order import Order
        from models.db_models.item import Item
        from models.db_models.setting import Setting

        classes = {
            'Order': Order,
            'Item': Item,
            'Setting': Setting
        }

        return(self.__store.find(classes[cls]))