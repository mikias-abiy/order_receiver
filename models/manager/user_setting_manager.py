#!/usr/bin/python3

"""
user_setting_manager:
    This module contains the defination of the UserSettingManager class.
"""


class UserSettingManager:
    """
    UserSettingManager: A model for object that manages / maps user to their
                  corresponding setting object.

    This is a documentation for the constructor method of this Class.
    Args:
        None
    """
    TOP_LEVEL = 0
    LANGUAGE_LEVEL = 1
    ORDERER_NAME_LEVEL = 2
    ORDERER_PHONE_LEVEL = 3
    ORDERER_ADDRESS_LEVEL = 4
    ORDERER_ITEM_NAME_LEVEL = 5
    ORDERER_ITEM_COLOR_LEVEL = 6
    ORDERER_ITEM_AMOUNT_LEVEL = 7

    # Language constants
    AMHARIC = 'am'
    ENGLISH = 'en'

    def __init__(self):
        self.__settings = {}

    def create_setting(self, user_id):
        """
        create_order: creats and entry and setting object with the user_id
                      provided.

        Args:
            user_id (int): The telegram id of the user.
        """
        from models.db_models.setting import Setting
        self.__settings[user_id] = Setting(user_id=user_id)

    def set_level(self, user_id, level):
        """
        set_level: sets the users current bot level setting.

        Args:
            user_id (int): The telegram id of the user.
            level (int): The current level.
        """
        self.__settings[user_id].level = level
        self.__settings[user_id].save()

    def set_language(self, user_id, language):
        """
        set_language: sets the users language setting.

        Args:
            user_id (int): The telegram id of the user.
            language (str): The language value of the user.
        """
        self.__settings[user_id].language = language
        self.__settings[user_id].save()


    def settings(self):
        """
        settings: return the dictionary of the user_id setting object pair.

        Args:
            None
        """
        return (dict(self.__settings))

    def get(self, user_id):
        """
        get: return the item with the provided user_id entry

        Args:
            user_id (int): The telegram id of the user.
        """
        if user_id in self.__settings.keys():
            return (self.__settings[user_id])
        else:
            return (None)

    def remove(self, user_id):
        """
        remove: removes an item from the dictionary.

        Args:
            user_id (int): The telegram id of the user.
        """
        del self.__settings[user_id]

    def reload(self):
        """
        reload: reloads previously registered settings before the bot stoped.
        """
        from models import storage

        settings = storage.get('Setting')

        for setting in settings:
            self.__settings[setting.user_id] = setting
