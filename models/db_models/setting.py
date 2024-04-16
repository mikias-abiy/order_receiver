#!/usr/bin/python3

"""
setting.py:
    This module contain the defination of the class Setting.
"""

import uuid
from datetime import datetime

from storm.locals import DateTime,\
    Int, Unicode, JSON, UUID

from models import storage

class Setting:
    '''
    Setting:
        Defination of class that contains setting information.
    '''
    __storm_table__ = 'settings'

    id = UUID(primary=True)
    created_at = DateTime()
    updated_at = DateTime()
    user_id = Int()
    level = Int(allow_none=True)
    language = Unicode(allow_none=True)

    def __init__(self, user_id, **kwargs):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.user_id = user_id
        self.level = 0
        self.language = 'am'
        storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()