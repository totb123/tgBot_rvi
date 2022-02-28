import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'roma real husoso')


@bot.message_handler(commands=["help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправь лайв локацию чтобы отметить посещение.')


# Получение сообщений от юзера и отправка списка команд
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, '_______СПИСОК КОМАНД_______\n'
                                      '/start - глаголит истину\n '
                                      '/help - инструкция\n')


@bot.message_handler(content_types=["location"])
def handle_location(message):
    print(message)
    location = message.location
    if location.live_period is not None:
        # тут условная долгота и широта я не ебу какая нужна и правильно ли написано тк не могу проверить.
        if 500 < location.longitude < 1000 and 500 < location.latitude < 1000:
            bot.send_message(message.chat.id, 'Посещение зачтено.')
        else:
            bot.send_message(message.chat.id, 'TI NE V UNIKE DURACHEK!!!!.')
        bot.send_message(message.chat.id, 'лайв тема шир дол \n here:')
        bot.send_location(message.chat.id, location.latitude, location.longitude)
    else:
        bot.send_message(message.chat.id, 'пришли лайв локацию')


if __name__ == '__main__':
    bot.infinity_polling()

# @bot.message_handler(content_types=["text"])
# def handle_group(message):
#     if BMSTU_API.group_name == 'ИУ6-42Б' and str(BMSTU_API.all_loc_guys.values()).find(message.text) != -1:
#         bot.send_message(message.chat.id, 'твоя группа: ' + BMSTU_API.group_name + '\nтебя зовут: ' + message.text)
#     else:
#         bot.send_message(message.chat.id, 'ты кто?')
