#!/usr/bin/python3

"""
order.py:
    This module contain the defination of the class Order.
"""

import uuid
from datetime import datetime

from storm.locals import DateTime,\
    Int, Unicode, JSON, UUID

from models import storage

class Order:
    '''
    Order:
        Defination of class that contains order information.
    '''
    __storm_table__ = 'orders'

    id = UUID(primary=True)
    created_at = DateTime()
    updated_at = DateTime()
    user_id = Int()
    name = Unicode(allow_none=True)
    phone = Unicode(allow_none=True)
    address = Unicode(allow_none=True)
    items = JSON(allow_none=True)

    def __init__(self, user_id, **kwargs):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.user_id = user_id
        self.name = kwargs.get('name', None)
        self.phone = kwargs.get('phone', None)
        self.address = kwargs.get('address', None)
        self.items = []
        storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()