#!/usr/bin/python3

# Standard modules and packages
import logging

# Local modules and packages
from bot import bot
import bot_commands

logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
    bot.infinity_polling()
