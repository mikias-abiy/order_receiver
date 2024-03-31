#!/usr/bin/python3

# Telegram telebot API module imports
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InputFile,\
    InputMediaPhoto

# Local modules imports
from bot import bot
from texts import AM, EN
from models import storage
from models import order_manager, user_setting_manager as usm
from helpers import items_name_list
from config import OWNER_USER_ID

# Done
@bot.message_handler(func=lambda message:
                     message.text in [
                         AM['cancle'], EN['cancle'], AM['done'],
                         EN['done'], '/start'
                     ])
def cmd_start(message):
    """
    cmd_start: starts the usm.and sends the set of keyboards to communicate
               with the usm.

    Args:
        message (Message: obj): The message object send from the user
    """
    if not usm.get(message.from_user.id):
        usm.create_setting(message.from_user.id)
        usm.set_language(message.from_user.id, usm.AMHARIC)
    
    usm.set_level(message.from_user.id, usm.TOP_LEVEL)

    texts = AM if usm.get(message.from_user.id).language == usm.AMHARIC else EN
    keys = texts['start_keys']

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton(keys[0]))
    markup.row(KeyboardButton(keys[1]), KeyboardButton(keys[2]))
    markup.row(KeyboardButton(keys[3]), KeyboardButton(keys[4]))

    if message.text in [AM['cancle'], EN['cancle']]:
        storage.remove(order_manager.get(message.from_user.id))
        order_manager.remove(message.from_user.id)
    elif message.text in [AM['done'], EN['done']]:
        bot.send_message(message.chat.id, texts['order_success'],
                         reply_markup=markup)
        return

    bot.send_message(message.chat.id, ':', reply_markup=markup)


# Done
@bot.message_handler(func=lambda message:
                     message.text == 'ስለ መተግበሪያው' or message.text == 'About'
                     and usm.get(message.from_user.id).level == usm.TOP_LEVEL)
def cmd_about(message):
    """
    cmd_about: sends a description about the usm.and the builder of the usm.

    Args:
        message (Message: obj): The message object send from the user
    """

    texts = AM if usm.get(message.from_user.id).language == usm.AMHARIC else EN

    bot.send_message(message.chat.id, texts['about'])


# Done
@bot.message_handler(func=lambda message:
                     message.text == 'Language' or message.text == 'ቋንቋ'
                     and usm.get(message.from_user.id).level == usm.TOP_LEVEL)
def cmd_language(message):
    """
    cmd_language: sends the available language options as a keyboard.

    Args:
        message (Message: obj): The message object send from the user
    """

    usm.get(message.from_user.id).level = usm.get(message.from_user.id).language_LEVEL

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton('አማርኛ'), KeyboardButton('English'))

    bot.send_message(message.chat.id, '/language', reply_markup=markup)


# Done
@bot.message_handler(func=lambda message:
                     message.text == 'አማርኛ' or message.text == 'English'
                     and usm.get(message.from_user.id).level == usm.get(message.from_user.id).language_LEVEL)
def cmd_change_language(message):
    """
    cmd_change_language: sets the language the user choose.

    Args:
        message (Message: obj): The message object send from the user
    """

    usm.get(message.from_user.id).language = usm.AMHARIC if message.text == 'አማርኛ' else usm.ENGLISH
    cmd_start(message)


# Done
@bot.message_handler(func=lambda message:
                     message.text == 'ዕቃዎች' or message.text == 'Items'
                     and usm.get(message.from_user.id).level == usm.TOP_LEVEL)
def cmd_items(message):
    """
    cmd_items: sends the availabe items to order from with pictures,
               price, name and other descriptions.

    Args:
        message (Message: obj): The message object send from the user
    """

    lang_key = 'am' if usm.get(message.from_user.id).language == usm.AMHARIC else 'en'
    texts = AM if usm.get(message.from_user.id).language == usm.AMHARIC else EN

    objects = storage.all()
    items = []

    for key, value in objects.items():
        if 'Item' in key:
            items.append(value)

    for item in items:
        medias = []
        for i in range(len(item.medias)):
            if i == 0:
                medias.append(InputMediaPhoto(media=InputFile(item.medias[i]),
                              caption=f"""
{texts['items_caption'][0]}: <b>{item.name[lang_key]}</b>
{texts['items_caption'][1]}: <b>{item.price}</b>""",
                              parse_mode="HTML"))
            else:
                medias.append(InputMediaPhoto(media=InputFile(item.medias[i])))
        bot.send_media_group(message.chat.id, media=medias)

    # bot.send_message(texts['size_description']


@bot.message_handler(func=lambda message:
                     message.text == 'ትዕዛዝ' or message.text == 'Order'
                     and usm.get(message.from_user.id).level == usm.TOP_LEVEL)
def cmd_order(message):
    """
    cmd_order: starts the ordering cycle of prompots.

    Args:
        message (Message: obj): The message object send from the user
    """
    texts = AM if usm.get(message.from_user.id).language == usm.AMHARIC else EN
    if order_manager.get(message.from_user.id) is not None:
        bot.send_message(message.chat.id, texts['previous_order'])
        return

    usm.get(message.from_user.id).level = usm.ORDERER_NAME_LEVEL

    prompot = texts['order_prompots']['orderer_name']

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton(f'{texts["cancle"]}'))

    bot.send_message(message.chat.id, prompot, reply_markup=markup)


@bot.message_handler(func=lambda message:
                     message.text not in ['cancle', 'ያቋርጡ'] and
                     usm.get(message.from_user.id).level == usm.ORDERER_NAME_LEVEL)
def cmd_set_name(message):
    """
    cmd_set_name: sets the name of the orderer to the order object.

    Args:
        message (Message: obj): The message object send from the user
    """

    texts = AM if usm.get(message.from_user.id).language == usm.AMHARIC else EN
    prompot = texts['order_prompots']['orderer_phone'][0]
    key = texts['order_prompots']['orderer_phone'][1]

    order_manager.create_order(message.from_user.id)

    order_manager.set_orderer_name(message.from_user.id, message.text)

    usm.get(message.from_user.id).level = usm.ORDERER_PHONE_LEVEL

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton(key, request_contact=True))
    markup.row(KeyboardButton(f'{texts["cancle"]}'))

    bot.send_message(message.chat.id, prompot, reply_markup=markup)


# Done
@bot.message_handler(func=lambda message: usm.get(message.from_user.id).level == usm.ORDERER_PHONE_LEVEL,
                     content_types=['contact'])
def cmd_set_phone(message):
    """
    cmd_set_phone: sets the phone of the orderer to the order object.

    Args:
        message (Message: obj): The message object send from the user
    """
    if usm.get(message.from_user.id).level != usm.ORDERER_PHONE_LEVEL:
        return

    texts = AM if usm.get(message.from_user.id).language == usm.AMHARIC else EN
    prompot = texts['order_prompots']['orderer_address']

    order_manager.set_orderer_phone(message.from_user.id,
                                    message.contact.phone_number)

    usm.get(message.from_user.id).level = usm.ORDERER_ADDRESS_LEVEL

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton(f'{texts["cancle"]}'))

    bot.send_message(message.chat.id, prompot, reply_markup=markup)


# Done
@bot.message_handler(func=lambda message:
                     (message.text not in ['cancle', 'ያቋርጡ'] and
                      usm.get(message.from_user.id).level == usm.ORDERER_ADDRESS_LEVEL) or
                     (message.text in [AM['add_order'], EN['add_order']]
                      and usm.get(message.from_user.id).level == usm.ORDERER_ITEM_AMOUNT_LEVEL))
def cmd_set_address(message):
    """
    cmd_set_address: sets the address of the orderer to the order object.

    Args:
        message (Message: obj): The message object send from the user
    """

    texts = AM if usm.get(message.from_user.id).language == usm.AMHARIC else EN
    prompot = texts['order_prompots']['item_name']
    lang_key = 'am' if usm.get(message.from_user.id).language == usm.AMHARIC else 'en'

    if message.text not in [AM['add_order'], EN['add_order']]:
        order_manager.set_orderer_address(message.from_user.id, message.text)

    usm.get(message.from_user.id).level = usm.ORDERER_ITEM_NAME_LEVEL

    objects = storage.all()
    items = []

    for key, value in objects.items():
        if 'Item' in key:
            items.append(value)

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(items) // 2, 2):
        markup.row(KeyboardButton(f'{items[i].name[lang_key]}'),
                   KeyboardButton(f'{items[i + 1].name[lang_key]}'))
    if len(items) % 2 != 0:
        markup.row(KeyboardButton(f'{items[-1].name[lang_key]}'))

    markup.row(KeyboardButton(f'{texts["cancle"]}'))

    bot.send_message(message.chat.id, prompot, reply_markup=markup)


# Done
@bot.message_handler(func=lambda message:
                     message.text in items_name_list() and
                     usm.get(message.from_user.id).level == usm.ORDERER_ITEM_NAME_LEVEL)
def cmd_set_item_name(message):
    """
    cmd_set_item_name: sets the name of the item the orderer ordered
                        to the order object.

    Args:
        message (Message: obj): The message object send from the user
    """
    texts = AM if usm.get(message.from_user.id).language == usm.AMHARIC else EN
    prompot = texts['order_prompots']['item_color']
    keys = texts['colors']

    order_manager.add_item(message.from_user.id, message.text)

    usm.get(message.from_user.id).level = usm.ORDERER_ITEM_COLOR_LEVEL

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for key in keys:
        markup.row(KeyboardButton(f'{key}'))
    markup.row(KeyboardButton(f'{texts["cancle"]}'))

    bot.send_message(message.chat.id, prompot, reply_markup=markup)


# Done
@bot.message_handler(func=lambda message:
                     message.text in AM['colors'] + EN['colors'] and
                     usm.get(message.from_user.id).level == usm.ORDERER_ITEM_COLOR_LEVEL)
def cmd_set_item_color(message):
    """
    cmd_set_item_color: sets the color of the item the orderer ordered
                        to the order object.

    Args:
        message (Message: obj): The message object send from the user
    """
    texts = AM if usm.get(message.from_user.id).language == usm.AMHARIC else EN
    prompot = texts['order_prompots']['item_amount']

    order_manager.set_item_color(message.from_user.id, message.text)

    usm.get(message.from_user.id).level = usm.ORDERER_ITEM_AMOUNT_LEVEL

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton(f'{texts["cancle"]}'))

    bot.send_message(message.chat.id, prompot, reply_markup=markup)


# Done
@bot.message_handler(func=lambda message:
                     message.text.isdigit() and
                     usm.get(message.from_user.id).level == usm.ORDERER_ITEM_AMOUNT_LEVEL)
def cmd_set_item_amount(message):
    """
    cmd_set_item_amount: sets the amount of the item the orderer ordered
                        to the order object.

    Args:
        message (Message: obj): The message object send from the user
    """
    texts = AM if usm.get(message.from_user.id).language == usm.AMHARIC else EN
    prompot = texts['order_prompots']['item_last']

    order_manager.set_item_amount(message.from_user.id, message.text)

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton(f'{texts["done"]}'),
               KeyboardButton(f'{texts["add_order"]}'))
    markup.row(KeyboardButton(f'{texts["cancle"]}'))

    bot.send_message(message.chat.id, prompot, reply_markup=markup)


@bot.message_handler(func=lambda message:
                     message.text in [EN['start_keys'][2], AM['start_keys'][2]] and
                     usm.get(message.from_user.id).level == usm.TOP_LEVEL)
def cmd_my_order(message):
    """
    cmd_my_order: sends the order of the user that is currently
                  communicating the usm.(if the user have any order).
    Args:
        message (Message: obj): The message object send from the user
    """
    texts = AM if usm.get(message.from_user.id).language == usm.AMHARIC else EN
    
    order = order_manager.get(message.from_user.id)

    if not order:
        bot.send_message(message.chat.id, texts['no_previous_order'])
    else:
        msg = f"""\
{texts['orders'][0]}: {order.name}
{texts['orders'][1]}: {order.phone}
{texts['orders'][2]}: {order.address}

{texts['orders'][3]}:
"""
        for i in range(len(order.items)):
            msg += f"   {i + 1}. {order.items[i]}\n"
        bot.send_message(message.chat.id, msg)
        
# Done
@bot.message_handler(commands=['all'],
                     func=lambda message: usm.get(message.from_user.id).level == usm.TOP_LEVEL)
def cmd_all_order(message):
    """
    cmd_all_order: sends all orders back. (Admin only)

    Args:
        message (Message: obj): The message object send from the user
    """
    if message.from_user.id != OWNER_USER_ID:
        return
    texts = AM if usm.get(message.from_user.id).language == usm.AMHARIC else EN
    orders = [value for value in order_manager.orders().values()]

    print(orders)

    for order in orders:
        msg = f"""\
{texts['orders'][0]}: {order.name}
{texts['orders'][1]}: {order.phone}
{texts['orders'][2]}: {order.address}

{texts['orders'][3]}:
"""
        for i in range(len(order.items)):
            msg += f"   {i + 1}. {order.items[i]}\n"
        bot.send_message(message.chat.id, msg)