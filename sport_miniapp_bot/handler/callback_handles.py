from answers import texts
from handler import callback_query_handler, collection_users
from telebot.types import CallbackQuery
from main import bot
from answers import keyboards
from challenges import collection_challenges, return_challenges
from . import message_handles


@callback_query_handler.state('default_admin')
def Type(callback: CallbackQuery, arg):
    # bot.send_message(callback.message.chat.id, texts.id)
    if callback.data == 'View':
        bot.send_message(callback.message.chat.id, texts.id)
        collection_users.update_one({"id": callback.from_user.id}, {"$set": {"state": 'default_admin(view)'}})
    if callback.data == 'Add':
        bot.send_message(callback.message.chat.id, texts.name, reply_markup=keyboards.remove)
        collection_users.update_one({"id": callback.from_user.id}, {"$set": {"state": 'default_admin(add)'}})
    if callback.data == 'Delete':
        bot.send_message(callback.message.chat.id, texts.id)
        collection_users.update_one({"id": callback.from_user.id}, {"$set": {"state": 'default_admin(delete)'}})


@callback_query_handler.state('goal')
def Type(callback: CallbackQuery):
    print([callback.data])
    if callback.data == 'Finish':
        print('qeweqw ')
        collection_challenges.insert_one(vars(message_handles.__dict__['new_challenge']))
        if collection_challenges.count_documents({}) == 0:
            print('huy')
            bot.send_message(callback.message.chat.id, "No active challenges", reply_markup=keyboards.challenges_markup)
        else:
            print('qwe')
            bot.send_message(callback.message.chat.id, "New challenge added", reply_markup=keyboards.admin_markup)
            challengs = return_challenges()
            for x in challengs[:-1]:
                bot.send_message(callback.message.chat.id, x)
            bot.send_message(callback.message.chat.id, challengs[-1],reply_markup=keyboards.challenges_markup)
            collection_users.update_one({"id": callback.from_user.id}, {"$set": {"state": 'default_admin()'}})
