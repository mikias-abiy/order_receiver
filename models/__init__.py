#!/usr/bin/python3

from dotenv  import load_dotenv


from models.engine import file_storage as fs
from models.manager import order_manager as om
from models.manager import user_setting_manager as usm

storage = fs.FileStorage()
storage.reload()

order_manager = om.OrderManager()
order_manager.reload()

user_setting_manager = usm.UserSettingManager()
user_setting_manager.reload()
