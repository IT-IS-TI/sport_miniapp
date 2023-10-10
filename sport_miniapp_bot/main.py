import config
from telebot import TeleBot, types
from handler import message_handler, callback_query_handler
from user import collection_users, User
from answers import texts,keyboards

bot = TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    # todo
    user_id = message.from_user.id
    user_db = collection_users.find_one({'id': user_id})
    if user_db == None:
        new_user = User(user_id)
        collection_users.insert_one(vars(new_user))
    collection_users.update_one({"id": message.from_user.id}, {"$set": {"state": "start"}})
    message_handler.handle(message)


@bot.message_handler(commands=['admin'])
def start(message: types.Message):
    # todo
    user_id = message.from_user.id
    user_db = collection_users.find_one({'id': user_id})
    if user_db == None:
        new_user = User(user_id)
        collection_users.insert_one(vars(new_user))
    collection_users.update_one({"id": message.from_user.id}, {"$set": {"state": "admin_authorization"}})
    message_handler.handle(message)


@bot.message_handler(commands=['sign_out'])
def start(message: types.Message):
    user_id = message.from_user.id
    user_db = collection_users.find_one({'id': user_id})
    if user_db == None:
        new_user = User(user_id)
        collection_users.insert_one(vars(new_user))
    message_handler.handle(message)
    collection_users.update_one({"id": message.from_user.id}, {"$set": {"login": ""}})
    collection_users.update_one({"id": message.from_user.id}, {"$set": {"password": ""}})
    bot.send_message(message.chat.id, texts.login, reply_markup=keyboards.remove)
    collection_users.update_one({"id": message.from_user.id}, {"$set": {"state": "authorization_login"}})




@bot.message_handler(content_types=['text'])
def message(mess: types.Message):
    message_handler.handle(mess)


@bot.callback_query_handler(lambda _: True)
def callback_query(callback: types.CallbackQuery):
    callback_query_handler.handle(callback)


if __name__ == '__main__':
    print('Bot started working')
    bot.polling(none_stop=True)
