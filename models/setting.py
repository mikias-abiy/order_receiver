#!/usr/bin/python3

"""
item.py: modules containes the defination of item class.
"""

from models.base_model import BaseModel


class Setting(BaseModel):
    """
    Setting:
        a class defination for Setting object.
    """

    def __init__(self, user_id, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
