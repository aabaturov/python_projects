import telebot
import config
from telebot import types
from sendings import send_name_message, send_id_message, send_photo_message, open_menu, send_sticker

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti1 = open('stickers/sticker1.webp', 'rb')
    bot.send_message(message.chat.id,
    "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, тестовый бот для обучения.\nДля взаимодействия со мной можешь воспользоваться меню".format(
    message.from_user, bot.get_me()), parse_mode='html')
    open_menu(message)
    
@bot.message_handler(commands=['stop'])
def stop(message):
    #bot.send_message(message.chat.id, 'Бот остановлен', reply_markup=telebot.types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item_start = types.KeyboardButton('/start')
    markup.add(item_start)
    bot.send_message(message.chat.id, "Бот остановлен", reply_markup = markup)  

@bot.message_handler(content_types=['audio', 'document', 'animation', 'game', 'photo', 'sticker', 'video', 'video_note', 'voice', 'contact', 'location', 'venue', 'dice', 'invoice', 'successful_payment', 'connected_website', 'poll', 'passport_data', 'web_app_data'])
def repeat(message):
    bot.send_message(message.chat.id, 'please, send command "Name", "Photo" or "Sticker"', parse_mode='html')

@bot.message_handler(content_types=['text'])
def repeat(message):
    text = message.text.lower()
    if (text == 'name'):
    	send_name_message(message)	
    elif (text == 'photo'):
    	send_photo_message(message) 
    elif (text == 'sticker'):
    	send_sticker(message)
    elif (text == 'open menu'):
    	open_menu(message)
    else:
        bot.send_message(message.chat.id, 'please, send command "Name", "Photo" or "Sticker"', parse_mode='html')
    	#bot.send_message(message.chat.id, 'err', parse_mode='html')
    #bot.send_message(message.chat.id, message.text, parse_mode='html')
     
#RUN
print('successfully started')
bot.polling(non_stop=True)
print('successfully stopped')
