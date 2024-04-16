#!/usr/bin/python3

"""
order_manager:
    This module contains the defination of the OrderManager class.
"""


class OrderManager:
    """
    OrderManager: A model for object that manages / maps user to their
                  corresponding order object.

    This is a documentation for the constructor method of this Class.
    Args:
        None
    """

    def __init__(self):
        self.__orders = {}

    def create_order(self, user_id):
        """
        create_order: creats and entry and order object with the user_id
                      provided.

        Args:
            user_id (int): The telegram id of the user.
        """
        from models.db_models.order import Order
        self.__orders[user_id] = Order(user_id=user_id)

    def set_orderer_name(self, user_id, name):
        """
        set_orderer_name: sets the orderers name.

        Args:
            user_id (int): The telegram id of the user.
            name (str): The name of the orderer
        """
        self.__orders[user_id].name = name
        self.__orders[user_id].save()

    def set_orderer_phone(self, user_id, phone):
        """
        set_orderer_phone: sets the orderers phone.

        Args:
            user_id (int): The telegram id of the user.
            phone (str): The phone number of the orderer.
        """
        self.__orders[user_id].phone = phone
        self.__orders[user_id].save()

    def set_orderer_address(self, user_id, address):
        """
        set_orderer_address: sets the orderers address.

        Args:
            user_id (int): The telegram id of the user.
            address (str): The address of the orderer.
        """
        self.__orders[user_id].address = address
        self.__orders[user_id].save()

    def add_item(self, user_id, name):
        """
        add_item: adds an item to the user order item collection.

        Args:
            user_id (int): The telegram id of the user.
            name (str): The name of the item.
        """
        if not getattr(self.__orders[user_id], 'items', None):
            self.__orders[user_id].items = []
        self.__orders[user_id].items.append([name])
        self.__orders[user_id].save()

    def set_item_color(self, user_id, color):
        """
        set_item_color: sets the color of the last added item to the users
                        item collection.
        Args:
            user_id (int): The telegram id of the user.
            color (str): The color of the item the user ordered.
        """
        self.__orders[user_id].items[-1].append(color)
        self.__orders[user_id].save()

    def set_item_amount(self, user_id, amount):
        """
        set_item_amount: sets the amount of the last added item to the
                         users item collection.

        Args:
            user_id (int): The telegram id of the user.
            amount (int): The amount of the item the user ordered.
        """
        self.__orders[user_id].items[-1].append(amount)
        self.__orders[user_id].save()

    def orders(self):
        """
        orders: return the dictionary of the user_id order object pair.

        Args:
            None
        """
        return (dict(self.__orders))

    def get(self, user_id):
        """
        get: return the item with the provided user_id entry

        Args:
            user_id (int): The telegram id of the user.
        """
        if user_id in self.__orders.keys():
            return (self.__orders[user_id])
        else:
            return (None)

    def remove(self, user_id):
        """
        remove: removes an item from the dictionary.

        Args:
            user_id (int): The telegram id of the user.
        """
        del self.__orders[user_id]

    def reload(self):
        """
        reload: reloads previously registered orders before the bot stoped.
        """
        from models import storage

        orders = storage.get('Order')

        for order in orders:
            self.__orders[order.user_id] = order
