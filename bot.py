import emoji
import telebot

import config
from parse import parse, get_coordinates

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def func(message):
    city = message.text
    if message.text == 'Писикак':
        bot.send_message(message.chat.id, emoji.emojize('Сейчас в городе Писикак:pig: 38 градусов по Цельсию'))
        bot.send_message(message.chat.id, emoji.emojize('Влажность носа 98%:pig_nose:'))
        return
    coordinates = get_coordinates(city)
    if not coordinates:
        bot.send_message(message.chat.id, 'Я не знаю такого города')
        return
    weather = parse(coordinates)
    temp = str(round(weather['main']['temp']))
    description = weather['weather'][0]['main']
    humidity = str(weather['main']['humidity'])
    bot.send_message(message.chat.id, 'Сейчас в городе ' + city + ' ' + temp + ' градусов по Цельсию')
    bot.send_message(message.chat.id, 'Влажность ' + humidity + '%')
    if description == 'Rain':
        bot.send_message(message.chat.id, emoji.emojize('Сейчас в городе ' + city + ' идет дождь. Не забудьте зонтик!:umbrella:'))

bot.polling(none_stop=True)