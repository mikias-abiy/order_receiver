#!/usr/bin/python3

from dotenv import dotenv_values

env_vars = dotenv_values('.env')

BOT_API_TOKEN = env_vars['BOT_API_TOKEN']
OWNER_USER_ID = env_vars['OWNER_USER_ID']