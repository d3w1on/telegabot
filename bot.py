import telebot
import config
from telebot import types
import json

bot = telebot.TeleBot(config.TOKEN)
scr_data = {}

with open('data/pizza.json', 'rb') as file:
    data = json.load(file)
    scr_data['pizza'] = data

with open('data/salads.json', 'rb') as file:
    data = json.load(file)
    scr_data['salads'] = data

with open('data/desserts.json', 'rb') as file:
    data = json.load(file)
    scr_data['desserts'] = data

with open('data/beverages.json', 'rb') as file:
    data = json.load(file)
    scr_data['beverages'] = data


@bot.message_handler(commands=['start'])
def greeting(message):
    usr = message.from_user.to_dict()
    greeting = f'Привіт, {usr["first_name"]}!\nМене звуть Орися, я допоможу тобі зробити у нас замовлення!'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    discounts = types.KeyboardButton('Акції')
    pizza = types.KeyboardButton('Піца')
    salads = types.KeyboardButton("Салати")
    dessert = types.KeyboardButton("Десерти")
    beverages = types.KeyboardButton("Напої")

    markup.add(discounts, pizza, salads, dessert, beverages)

    with open('sticker.webp', 'rb') as sti:
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, greeting, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.chat.type == 'private':
        if message.text == 'Акції':
            discounts(message)
        elif message.text == 'Піца':
            pizza(message)
        elif message.text == 'Салати':
            salads(message)
        elif message.text == 'Десерти':
            desserts(message)
        elif message.text == 'Напої':
            beverages(message)


@bot.message_handler(content_types=['text'])
def discounts(message):
    with open('data/discount.json', 'rb') as file:
        data = json.load(file)
        for i in data:
            markup = types.InlineKeyboardMarkup(row_width=1)
            item = types.InlineKeyboardButton('Cкористатися', url=i['link'])

            markup.add(item)
            bot.send_photo(message.chat.id, i['img'])
            bot.send_message(message.chat.id, i['text'], reply_markup=markup)


@bot.message_handler(content_types=['text'])
def pizza(message):
    reply_text = 'Фотографії продуктів несуть ознайомчий характер і можуть відрізнятися від оригіналу'
    with open('data/pizza.json', 'rb') as file:
        data = json.load(file)

        markup = types.InlineKeyboardMarkup(row_width=4)
        for i in range(len(scr_data['pizza'])):
            btn_txt = f"{data[i]['name']} - {data[i]['price']}"
            item = types.InlineKeyboardButton(btn_txt, callback_data=str(scr_data['pizza'][i]['id']))
            markup.add(item)

        bot.send_photo(message.chat.id, data[0]['img'])
        bot.send_message(message.chat.id, text=reply_text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def salads(message):
    reply_text = 'Боїтеся помилитися та обрати не той салат? Зателефонуйте до доставки піци «Lа П’єц» у Львові та ' \
                 'проконсультуйтеся перед тим, як зробити замовлення. '

    with open('data/salads.json', 'rb') as file:
        data = json.load(file)

        markup = types.InlineKeyboardMarkup(row_width=4)
        for i in range(len(scr_data['salads'])):
            btn_txt = f"{data[i]['name']} - {data[i]['price']}"
            item = types.InlineKeyboardButton(btn_txt, callback_data=str(scr_data['salads'][i]['id']))
            markup.add(item)

        bot.send_photo(message.chat.id, data[0]['img'])
        bot.send_message(message.chat.id, text=reply_text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def desserts(message):
    reply_text = 'Десерти:'
    with open('data/desserts.json', 'rb') as file:
        data = json.load(file)

        markup = types.InlineKeyboardMarkup(row_width=4)
        for i in range(len(scr_data['desserts'])):
            btn_txt = f"{scr_data['desserts'][i]['name']} - {scr_data['desserts'][i]['price']}"
            item = types.InlineKeyboardButton(btn_txt, callback_data=scr_data['desserts'][i]['id'])
            markup.add(item)

        bot.send_photo(message.chat.id, data[0]['img'])
        bot.send_message(message.chat.id, text=reply_text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def beverages(message):
    reply_text = 'Напої:'
    with open('data/beverages.json', 'rb') as file:
        data = json.load(file)

        markup = types.InlineKeyboardMarkup(row_width=4)
        for i in range(len(scr_data['beverages'])):
            btn_txt = f"{scr_data['beverages'][i]['name']} - {scr_data['beverages'][i]['price']}"
            item = types.InlineKeyboardButton(btn_txt, callback_data=scr_data['beverages'][i]['id'])
            markup.add(item)

        bot.send_photo(message.chat.id, data[0]['img'])
        bot.send_message(message.chat.id, text=reply_text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def msg_callback(call):


    try:
        if call.message:
            for i in range(len(scr_data['pizza'])):
                if call.data == str(scr_data['pizza'][i]['id']):
                    msg_template = f'{scr_data["pizza"][i]["name"]}\n{scr_data["pizza"][i]["desc"]}\nЦіна: {scr_data["pizza"][i]["price"]}\nРозмір: {scr_data["pizza"][i]["size"]}\nВага: {scr_data["pizza"][i]["weight"]}'
                    markup = types.InlineKeyboardMarkup(row_width=4)
                    item = types.InlineKeyboardButton('Дивитись на сайті', url=scr_data['pizza'][i]['link'])
                    markup.add(item)
                    bot.send_photo(call.message.chat.id, scr_data['pizza'][i]['img'])
                    bot.send_message(call.message.chat.id, msg_template, reply_markup=markup)

            for i in range(len(scr_data['salads'])):
                if call.data == str(scr_data['salads'][i]['id']):
                    msg_template = f'{scr_data["salads"][i]["name"]}\n{scr_data["salads"][i]["desc"]}\nЦіна: {scr_data["salads"][i]["price"]}\nВага: {scr_data["salads"][i]["weight"]}'

                    bot.send_photo(call.message.chat.id, scr_data['salads'][i]['img'])
                    bot.send_message(call.message.chat.id, msg_template)
            for i in range(len(scr_data['beverages'])):
                if call.data == str(scr_data['beverages'][i]['id']):
                    msg_template = f'{scr_data["beverages"][i]["name"]}\nЦіна: {scr_data["beverages"][i]["price"]}'
                    # markup = types.InlineKeyboardMarkup(row_width=4)
                    # item = types.InlineKeyboardButton('Дивитись на сайті', url=scr_data['beverages'][i]['link'])
                    # markup.add(item)
                    bot.send_photo(call.message.chat.id, scr_data['beverages'][i]['img'])
                    bot.send_message(call.message.chat.id, msg_template)
            for i in range(len(scr_data['desserts'])):
                if call.data == str(scr_data['desserts'][i]['id']):
                    msg_template = f'{scr_data["desserts"][i]["name"]}\n{scr_data["desserts"][i]["desc"]}\nВага: {scr_data["desserts"][i]["desc"]}\nЦіна: {scr_data["desserts"][i]["price"]}'
                    # markup = types.InlineKeyboardMarkup(row_width=4)
                    # item = types.InlineKeyboardButton('Дивитись на сайті', url=scr_data['desserts'][i]['link'])
                    # markup.add(item)
                    bot.send_photo(call.message.chat.id, scr_data['desserts'][i]['img'])
                    bot.send_message(call.message.chat.id, msg_template)
    except Exception as e:
        print(e)







if __name__ == '__main__':
    bot.polling(none_stop=True)
