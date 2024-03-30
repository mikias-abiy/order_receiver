#!/usr/bin/python3

import telebot


class Bot(telebot.TeleBot):
    """
    Bot: Class inherits from the telebot.Telebot and contains specific
         Attributes and methods to this specific bot.
    
    This is a documentation for the constructor method of this Class.
    Args:
        token (str): The telegram bot API token.
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

    def __init__(self, token, **kwargs):
        super().__init__(token, **kwargs)
        self.__level = self.__class__.TOP_LEVEL
        self.__language = self.__class__.AMHARIC

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        # Value cheking needed
        self.__level = value

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        # Value cheking needed
        self.__language = value
