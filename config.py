#!/usr/bin/python3

from dotenv import dotenv_values

F_ENV = '.env'

env_vars = dotenv_values(F_ENV)

BOT_API_TOKEN = env_vars['BOT_API_TOKEN']
OWNER_USER_ID = env_vars['OWNER_USER_ID']