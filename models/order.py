#!/usr/bin/python3

"""
order.py: modules containes the defination of order class.
"""

from models.base_model import BaseModel


class Order(BaseModel):
    """
    Order:
        a class defination for Order object.
    
    This is a documentation for the constructor method of this Class.
    Args:
        user_id (int): The telegram id of the user.
    """

    def __init__(self, user_id, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
