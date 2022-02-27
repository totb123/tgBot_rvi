import telebot
impo

# Создаем экземпляр бота
bot = telebot.TeleBot('5129003895:AAFR9AFYjPFaAnBBWypVWXziMQzAmicHRjU')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'привет')


# Получение сообщений от юзера
#@bot.message_handler(content_types=["text"])
#def handle_text(message):
#    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

@bot.message_handler(content_types=["text"])
def handle_group(message):
    if BMSTU_API.group_name == 'ИУ6-42Б' and str(BMSTU_API.all_loc_guys.values()).find(message.text) != -1 :
        bot.send_message(message.chat.id, 'твоя группа: ' + BMSTU_API.group_name + '\nтебя зовут: ' + message.text)
    else:
        bot.send_message(message.chat.id, 'ты кто?')

@bot.message_handler(content_types=["location"])
def handle_location(message):
    print(message)
    location = message.location
    if location.live_period != None:
        bot.send_message(message.chat.id, 'wow you are in class \n here:')
        bot.send_location(message.chat.id, location.latitude, location.longitude)
    else:
        bot.send_message(message.chat.id, 'Send me live location')


if __name__ == '__main__':
    bot.infinity_polling()
