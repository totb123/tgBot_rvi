import telebot
import config

# Тут для тебя друг мой подсказка используй сочитание клавиш 'cntr + alt + L'
# И напиши если не впадлу на всякий команды git в этот комент ЦЕЛУЮ!!!

bot = telebot.TeleBot(config.TOKEN)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'roma real husoso')


# сверху писал позер цитата->
# Функция, обрабатывающая команду /help
@bot.message_handler(commands=["help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправь лайв локацию чтобы отметить посещение.')


# Получение сообщений от юзера и отправка списка команд
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, '_______СПИСОК КОМАНД_______\n'
                                      '/start - глаголит истину\n '
                                      '/help - инструкция\n')
    # НУ Я БОЛЬШЕ И НЕПРИДУМАЛ НО ЭТО И НЕ НАДО ПРОСТО ТЕСТОВАЯ ХЕРЬ ТАК ЧТО ЗАБЕЙ МОЖЕШЬ ДЕЛИТНУТЬ))))


# Одна из основных функций связанной с обработкой  геолокацией пользователя естественно нихрена не работает(пока что:3)
@bot.message_handler(content_types=["location"])
def handle_location(message):
    poseshenie = None
    print(message)
    location = message.location
    if location.live_period is not None:
        # тут условная долгота и широта я не ебу какая нужна и правильно ли написано тк не могу проверить.
        if 500 < location.longitude < 1000 and 500 < location.latitude < 1000:
            bot.send_message(message.chat.id, 'Посещение зачтено.'
                                              'лайв тема шир дол \n here:'
                             , location.latitude, location.longitude)
        # я кстаи еще не понял как выводить данные или запрашивать или отправлять тоесть ты меня понял крч.
        else:
            bot.send_message(message.chat.id, 'TI NE V UNIKE DURACHEK!!!!'
                                              'лайв тема шир дол \n here:'
                             , location.latitude, location.longitude)
    else:
        bot.send_message(message.chat.id, 'пришли лайв локацию'
                                          'offline тема шир дол \n here:'
                         , location.latitude, location.longitude)


if __name__ == '__main__':
    bot.infinity_polling()

# @bot.message_handler(content_types=["text"])
# def handle_group(message):
#     if BMSTU_API.group_name == 'ИУ6-42Б' and str(BMSTU_API.all_loc_guys.values()).find(message.text) != -1:
#         bot.send_message(message.chat.id, 'твоя группа: ' + BMSTU_API.group_name + '\nтебя зовут: ' + message.text)
#     else:
#         bot.send_message(message.chat.id, 'ты кто?')
