import telebot
import config

# Тут для тебя друг мой подсказка используй сочитание клавиш 'cntr + alt + L' она тип порядок наводит

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=["location"])
def location(message):
    location_of_user = message.location
    if location_of_user.live_period is not None:
        # так тут мы преобразуем идиотскую инфу в обычные переменные чтобы можно было бы их использовать.
        dolgota = float("%s" % (location_of_user.longitude))
        shirota = float("%s" % (location_of_user.latitude))
        print(type(dolgota))
        print(dolgota)
        # Короче здесь мои корды и я типа в унике вот туда нужно будет вбить рил корды нужные и сделать функцию поидее
        # которая будет то ли в базу данных заносить инфу о посещении или там отправлять запрос тип он посетил итд
        if 37.6 < dolgota < 37.7 and 55.7 < shirota < 55.72:
            bot.send_message(message.chat.id, 'Ты в унике')
        else:
            # кстати попробуй запустить бота и отправить локацию свою на эти корды поидее должен этот вариант сыграть
            bot.send_message(message.chat.id, 'TI NE V UNIKE DURACHEK!!!!!')
    else:
        bot.send_message(message.chat.id, 'отправь live-локацию')
        # это чтобы ты узнал свои корды
        dolgota = ("%s" % (location_of_user.longitude))
        shirota = ("%s" % (location_of_user.latitude))
        print(dolgota, shirota)


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


if __name__ == '__main__':
    bot.infinity_polling()

# @bot.message_handler(content_types=["text"])
# def handle_group(message):
#     if BMSTU_API.group_name == 'ИУ6-42Б' and str(BMSTU_API.all_loc_guys.values()).find(message.text) != -1:
#         bot.send_message(message.chat.id, 'твоя группа: ' + BMSTU_API.group_name + '\nтебя зовут: ' + message.text)
#     else:
#         bot.send_message(message.chat.id, 'ты кто?')
