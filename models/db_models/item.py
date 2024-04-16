#!/usr/bin/python3

"""
item.py:
    This module contain the defination of the class Item.
"""

import uuid
from datetime import datetime

from storm.locals import DateTime,\
    Int, JSON, UUID

from models import storage

class Item:
    '''
    Item:
        Defination of class that contains item information.
    '''
    __storm_table__ = 'items'

    id = UUID(primary=True)
    created_at = DateTime()
    updated_at = DateTime()
    name = JSON()
    price = Int()
    medias = JSON(allow_none=True)

    def __init__(self, name, price, medias):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.name = name
        self.price = price
        self.medias = medias
        storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()