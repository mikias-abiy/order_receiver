#!/usr/bin/python3


from models import storage


def items_name_list():
    """
    items_name_list: extracts list of the names of the items that are stored on the storage.
    """
    objects = storage.all()
    items = []

    for key, value in objects.items():
        if 'Item' in key:
            items.append(value.name['am'])
            items.append(value.name['en'])

    return (items)
