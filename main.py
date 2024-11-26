from telebot import TeleBot

bot = TeleBot('7578153252:AAHvmQdzYArBZmEKGkEzftxMROnTzZpoZeU')

@bot.message_handler(commands=['start'])
def botic(message):
    bot.send_message(message.chat.id, "*Привет!*\nСпасибо, что написал мне!", parse_mode='Markdown')


@bot.message_handler(commands=['python'])
def botic(message):
    bot.send_message(message.chat.id, 'Вот все о питонах\nhttps://ru.wikipedia.org/wiki/Питоны')


@bot.message_handler(commands=['спасибо'])
def botic(message):
    bot.send_message(message.chat.id, 'Не за что!')


@bot.message_handler(commands=['как дела'])
def botic(message):
    bot.send_message(message.chat.id, 'Спасибо, что спросил!\nУ меня все хорошо')


@bot.message_handler(commands=['пока'])
def botic(message):
    bot.send_message(message.chat.id, 'Окей, тогда до встречи!')



bot.infinity_polling()