#!/usr/bin/python3


from models import storage


def items_name_list():
    """
    items_name_list: extracts list of the names of the items that are stored on the storage.
    """
    objects = storage.get('Item')

    items = []

    for obj in objects:
        items.append(obj.name['am'])
        items.append(obj.name['en'])

    return (items)
