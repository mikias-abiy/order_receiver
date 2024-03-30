#!/usr/bin/python3

"""
item.py: modules containes the defination of item class.
"""

from models.base_model import BaseModel


class Item(BaseModel):
    """
    Item:
        a class defination for Item object.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
