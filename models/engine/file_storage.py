#!/usr/bin/python3

"""
file_storage:
    This module holds the defination of the class FileStorage
    which handles the storage of objects.
"""


import json


class FileStorage:
    """
    FileStorage: handles object storage persistency

    Attributes:
        __file_path (str): path to the json file holding the objects
                           json representation.
       __objects (dict): Dictionary holding the objects.
    """

    __objects = {}
    __file_path = 'storage.json'

    def all(self, types=None):
        """
        all(self):
            Returns dictionary of the objects stored.

        Return:
            Dictionry of the the stored objects.
        """
        objects = {}
        if types:
            for typ in types:
                for key in FileStorage.__objects.keys():
                    if typ in key:
                        objects[key] = FileStorage.__objects[key]

        else:
            objects = dict(FileStorage.__objects)
        return (objects)

    def new(self, obj):
        """
        new:
            Inserts new object to the collection of objects.

        Args:
            obj: The object to be stored.

        Return:
            None.
        """
        FileStorage.__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def remove(self, obj):
        """
        remove:
            Removes an object from the collection of objects.

        Args:
            obj: The object to be stored.

        Return:
            None.
        """
        FileStorage.__objects.pop(f'{type(obj).__name__}.{obj.id}')
        self.save()

    def save(self):
        """
        save(self):
            Saves the objects collection dictionary in to a file
            after converting it to a json representation.

        Return:
            None.
        """
        with open(FileStorage.__file_path, 'w') as file:
            to_serialize = FileStorage.__objects.copy()
            for key in to_serialize.keys():
                to_serialize[key] = to_serialize[key].to_dict()
            file.write(json.dumps(to_serialize))

    def reload(self):
        """
        reload(self):
            Reloads the objects from the last saved file that
            that contains the json representation of the objects.
        """
        from models.base_model import BaseModel
        from models.order import Order
        from models.item import Item

        classes = {"Order": Order, "Item": Item}
        try:
            with open(FileStorage.__file_path, 'r') as file:
                _raw = json.load(file)
                for key in _raw.keys():
                    _raw[key] = classes[_raw[key]['__class__']](**_raw[key])
                FileStorage.__objects = _raw
        except FileNotFoundError:
            pass
