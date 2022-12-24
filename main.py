import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import random

TOKEN = "5825862970:AAE86fdW1VAITzXsrRMlva5WirD_HiXXvwg"


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    global page
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Next Page👉')
    item2 = types.KeyboardButton('Previous Page👈')
    item3 = types.KeyboardButton('Random Page🎲')
    page =0
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Press "Next Page👉" to go to the first page', reply_markup=markup)
            
@bot.message_handler(content_types=['text'])
def bot_message(message):
    global page
    if message.chat.type =='private':
        if message.text == 'Next Page👉':
            page +=1
            post = f"https://www.1001fonts.com/free-for-commercial-use-fonts.html?page={page}"
            response = requests.get(post)
            soup = BeautifulSoup(response.text, "lxml")
            try:
                for link in soup.find_all('img'):
                # display the actual urls
                    if link.attrs['src'] != '//st.1001fonts.net/img/1001fonts-logo.svg':
                        print('https:' + link.attrs['src']) 
                        bot.send_photo(message.chat.id, "https:" + link.attrs['src'])
            except:
                    bot.send_message(message.chat.id, f"The photo of font is not available right now.")
            bot.send_message(message.chat.id, f"It's {page} page \n \nhttps://www.1001fonts.com/free-for-commercial-use-fonts.html?page={page}")
        if message.text == 'Previous Page👈':
            if page >1:
                page -=1
                post = f"https://www.1001fonts.com/free-for-commercial-use-fonts.html?page={page}"
                response = requests.get(post)
                soup = BeautifulSoup(response.text, "lxml")
                try:
                    for link in soup.find_all('img'):
                    # display the actual urls
                        if link.attrs['src'] != '//st.1001fonts.net/img/1001fonts-logo.svg':
                            print('https:' + link.attrs['src']) 
                            bot.send_photo(message.chat.id, "https:" + link.attrs['src'])
                except:
                    bot.send_message(message.chat.id, f"The photo of font is not available right now.")
                bot.send_message(message.chat.id, f"It's {page} page \n \nhttps://www.1001fonts.com/free-for-commercial-use-fonts.html?page={page}")
            else:
                bot.send_message(message.chat.id, 'It was first page!')
        if message.text == 'Random Page🎲':
            page =random.randint(1,500)
            post = f"https://www.1001fonts.com/free-for-commercial-use-fonts.html?page={page}"
            response = requests.get(post)
            soup = BeautifulSoup(response.text, "lxml")
            for link in soup.find_all('img'):
            # display the actual urls
                try:
                    if link.attrs['src'] != '//st.1001fonts.net/img/1001fonts-logo.svg':
                        print('https:' + link.attrs['src']) 
                        markup2 = types.ReplyKeyboardMarkup(resize_keyboard = True)
                        wtpg = types.KeyboardButton('What page is it?')
                        markup2.add(wtpg)
                        bot.send_photo(message.chat.id, "https:" + link.attrs['src'], reply_markup=markup2)
                except:
                    mm = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    wtpg2 = types.KeyboardButton('What page is it?')
                    mm.add(wtpg2)
                    bot.send_message(message.chat.id, f"The photo of font is not available right now.", reply_markup=mm)
                    

        if message.text == 'What page is it?':
            markup3 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            pon = types.KeyboardButton('Pon')
            markup3.add(pon)
            bot.send_message(message.chat.id, f"It's {page} page \n \nhttps://www.1001fonts.com/free-for-commercial-use-fonts.html?page={page}", reply_markup=markup3)
            print(1)
        if message.text == 'Pon':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Next Page👉')
            item2 = types.KeyboardButton('Previous Page👈')
            item3 = types.KeyboardButton('Random Page🎲')
            page =0
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Press "Next Page👉" to go to the first page', reply_markup=markup)
bot.polling(non_stop=True)