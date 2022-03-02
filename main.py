import telebot
import config

# Тут для тебя друг мой подсказка используй сочитание клавиш 'cntr + alt + L' она тип порядок наводит

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=["location"])
def location(message):
    location_of_user = message.location
    if location_of_user.live_period is not None:
        print(message.location)
        dolgota = "%s" % (location_of_user.longitude)
        shirota = "%s" % (location_of_user.latitude)
        # БЛЯТЬ ЭТО ЧТО КЕКИС ЧТО ЗА ХУЙНЯ БЛЯТЬ ЧЕЛ ОН ПРОСТО НЕ ПРИВОДИТСЯ К ФЛОТУ
        float(dolgota)
        float(shirota)
        print(type(dolgota))
        print(dolgota)
        # if 35 < dolgota < 40 and 50 < shirota < 60:
        #     bot.send_message(message.chat.id, 'Ты в унике')
        # else:
        #     bot.send_message(message.chat.id, 'TI NE V UNIKE DURACHEK!!!!!')
    else:
        bot.send_message(message.chat.id, 'отправь live-локацию')


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
