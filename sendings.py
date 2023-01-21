import telebot
import config
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

def send_name_message(message):
    bot.send_message(message.chat.id,
    "Сообщение 1.\nВаше имя - {0.first_name}!\nМоё имя(жирным) - <b>{1.first_name}</b>.".format(
    message.from_user, bot.get_me()), parse_mode='html')
    
def send_id_message(message):
    bot.send_message(message.chat.id,
    "Сообщение 2.\nВаш айди - , {0.id}!\nМой айди(жирным) - <b>{1.id}</b>.".format(
    message.from_user, bot.get_me()), parse_mode='html')    

def send_photo_message(message):
    number = bot.get_user_profile_photos(message.from_user.id)
    bot.send_message(message.chat.id, 
    "Сообщение 2.\nВаше фото", parse_mode='html')
    photos_ids = []
    for photo in number.photos:
        photos_ids.append(photo[0].file_id)    
    bot.send_photo(message.chat.id, photos_ids[random.randint(0,number.total_count - 1)])
    
def open_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item_name = types.KeyboardButton('Name')
    item_photo = types.KeyboardButton('Photo')
    item_sticker = types.KeyboardButton('Sticker')
    item_exit = types.KeyboardButton('/stop')    
    markup.add(item_name, item_photo, item_sticker, item_exit)
    
    bot.send_message(message.chat.id, "Бот запущен", reply_markup = markup)  

def send_sticker(message):
    rand = random.randint(1,5)
    if (rand == 1):
        sti = open('stickers/sticker1.webp', 'rb')
    if (rand == 2):
        sti = open('stickers/sticker2.webp', 'rb')
    if (rand == 3):
        sti = open('stickers/sticker3.webp', 'rb')
    if (rand == 4):
        sti = open('stickers/sticker4.webp', 'rb')
    if (rand == 5):
        sti = open('stickers/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
