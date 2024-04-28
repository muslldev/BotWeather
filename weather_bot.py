import telebot
import requests
import json

TOKEN = '6717290476:AAHQYrT2a2qyENNl-cFK3N0GTy78-iw97Ug'
API = 'eeb7e283c831eeb1f11abbc6230edce2'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Напиши город.')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
     data = json.loads(res.text)
     temp = data['main']['temp']
     bot.send_message(message.chat.id, f'Сейчас погода: {temp} C')
    else:
     bot.send_message(message.chat.id, f'Город указан неверно')

bot.infinity_polling()