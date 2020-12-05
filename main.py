import telebot

bot = telebot.TeleBot('1412005435:AAFbs3EVuTxJhszv-vUP7oDrpl7gzCOuMdY')


@bot.message_handler(content_types=['text'])
def get_text_massages (message):

    print(message)
    bot.send_message(message.from_user.id, message.json["text"])
    if message.json =="Привет":
        bot.send_message(message.from_user.id, "Привет")
    if message.json =="text":
        bot.send_message(message.from_user.id, "Я тебя не понимаю")

bot.polling(none_stop=True, interval=0)
