import re
from challenges import return_challenges
import challenges
from handler import message_handler, collection_users
from main import bot
from answers import texts, keyboards
from answers.texts import emoji
from telebot.types import Message
from re import fullmatch, match
import take_hours
from challenges import collection_challenges
from challenges import Challenge


@message_handler.state('start')
def default(message: Message):
    if message.text == '/start':
        collection_users.update_one({"id": message.from_user.id}, {"$set": {"state": "default"}})
        bot.send_message(message.chat.id, texts.greetings, reply_markup=keyboards.default_markup)


@message_handler.state('default')
def start_page(message: Message):
    id = message.from_user.id
    if message.text == 'About':
        bot.send_message(message.chat.id, texts.About_Button, reply_markup=keyboards.default_markup)
    if message.text == 'Help':
        bot.send_message(message.chat.id, texts.Help_Button, reply_markup=keyboards.default_markup)
    if message.text == 'Sign in':
        if collection_users.find_one({'id': id})["login"] == '':
            collection_users.update_one({"id": message.from_user.id}, {"$set": {"state": 'authorization_login'}})
            bot.send_message(message.chat.id, texts.login, reply_markup=keyboards.remove)
        elif collection_users.find_one({'id': id})["login"] != '' and collection_users.find_one({'id': id})[
            "password"] == '':
            collection_users.update_one({"id": message.from_user.id}, {"$set": {"state": 'authorization_password'}})
            bot.send_message(message.chat.id, texts.password, reply_markup=keyboards.remove)
        else:
            collection_users.update_one({"id": message.from_user.id}, {"$set": {"state": 'default2'}})
            bot.send_message(message.chat.id, texts.already_registered, reply_markup=keyboards.default_markup2)
    if message.text == '/start':
        bot.send_message(message.chat.id, texts.greetings, reply_markup=keyboards.default_markup)


@message_handler.state('authorization_login')
def authorization_page_login(message: Message):
    id = message.from_user.id
    txt = message.text.lower()
    if message.text == '/start':
        collection_users.update_one({"id": message.from_user.id}, {"$set": {"state": 'default'}})
        bot.send_message(message.chat.id, texts.greetings, reply_markup=keyboards.default_markup)
    if fullmatch('[a-z]+.[a-z]+@innopolis.university', txt) or fullmatch('[a-z]+.[a-z]+@innopolis.ru', txt):
        collection_users.update_one({"id": message.from_user.id}, {"$set": {"state": 'authorization_password'}})
        collection_users.update_one({"id": id}, {"$set": {"login": message.text}})
        # print(collection_users.find_one({'id': id}.__dict__))
        bot.send_message(message.chat.id, texts.password, reply_markup=keyboards.remove)
    else:
        bot.send_message(message.chat.id, '''Incorrect Innopolis email''',
                         reply_markup=keyboards.remove)


@message_handler.state('authorization_password')
def authorization_page_password(message: Message):
    id = message.from_user.id
    collection_users.update_one({"id": message.from_user.id}, {"$set": {"state": 'default2'}})
    collection_users.update_one({"id": id}, {"$set": {"password": message.text}})
    bot.send_message(message.chat.id, texts.regirstation)
    bot.delete_message(message.chat.id, message.message_id)
    if take_hours.update(id) == 'Error':
        bot.send_message(message.chat.id, "You are not a student", reply_markup=keyboards.default_markup2)
    else:
        bot.send_message(message.chat.id, texts.registered, reply_markup=keyboards.default_markup2)

    if message.text == '/start':
        bot.send_message(message.chat.id, texts.greetings, reply_markup=keyboards.default_markup2)


@message_handler.state('default2')
def start_page2(message: Message):
    id = message.from_user.id
    if message.text == '/start':
        bot.send_message(message.chat.id, texts.greetings, reply_markup=keyboards.default_markup2)
    if message.text == 'About':
        bot.send_message(message.chat.id, texts.About_Button, reply_markup=keyboards.default_markup2)
    if message.text == 'Help':
        bot.send_message(message.chat.id, texts.Help_Button, reply_markup=keyboards.default_markup2)
    if message.text == 'Profile':
        print('Profile button pressed')
        bot.send_message(message.chat.id, texts.Profile, reply_markup=keyboards.Profile_markup)


@message_handler.state('admin_authorization')
def admin_page(message: Message):
    id = message.from_user.id
    bot.send_message(message.chat.id, texts.admin_password)
    collection_users.update_one({"id": id}, {"$set": {"state": 'adminka'}})


@message_handler.state('adminka')
def start_page(message: Message):
    id = message.from_user.id
    if message.text == '192348576':
        collection_users.update_one({"id": id}, {"$set": {"state": 'default_admin()'}})
        bot.send_message(message.chat.id, texts.login_successful, reply_markup=keyboards.admin_markup)
    else:
        bot.send_message(message.chat.id, texts.wrong_password)


@message_handler.state('default_admin')
def start_page(message: Message, arg):
    id = message.from_user.id
    if message.text == '/start':
        bot.send_message(message.chat.id, texts.greetings, reply_markup=keyboards.admin_markup)
    elif message.text == 'About':
        bot.send_message(message.chat.id, texts.About_Button, reply_markup=keyboards.admin_markup)
    elif message.text == 'Help':
        bot.send_message(message.chat.id, texts.Help_Button, reply_markup=keyboards.admin_markup)
    elif message.text == 'Profile':
        bot.send_message(message.chat.id, texts.Profile, reply_markup=keyboards.Profile_markup)
    elif message.text == 'Challenges':
        if collection_challenges.count_documents({}) == 0:
            bot.send_message(message.chat.id, "No active challenges", reply_markup=keyboards.challenges_markup)
        else:
            challengs = return_challenges()
            for x in challengs[:-1]:
                bot.send_message(message.chat.id, x)
            bot.send_message(message.chat.id, challengs[-1], reply_markup=keyboards.challenges_markup)
    elif arg == 'view':
        bot.send_message(message.chat.id, challenges.return_one_challenge(message.text))
    elif arg == 'add':
        global new_challenge
        new_challenge = Challenge(message.text)
        collection_users.update_one({"id": id},
                                    {"$set": {"state": 'short_description'}})
        bot.send_message(message.chat.id, texts.short_description)
    elif arg == 'delete':
        if re.match(r'^[-+]?\d+$', message.text):
            if collection_challenges.find_one({"id": message.text}) != None:
                collection_challenges.delete_one({"id": message.text})
                bot.send_message(message.chat.id, "The challenge is deleted", reply_markup=keyboards.remove)
                # lst.clear()
                if collection_challenges.count_documents({}) == 0:
                    bot.send_message(message.chat.id, "No active challenges", reply_markup=keyboards.challenges_markup)
                else:
                    challengs = return_challenges()
                    for x in challengs[:-1]:
                        bot.send_message(message.chat.id, x)
                    bot.send_message(message.chat.id, challengs[-1], reply_markup=keyboards.challenges_markup)
            else:
                bot.send_message(message.chat.id, "No such challenge")
        else:
            bot.send_message(message.chat.id, "Please write the number")

        # проверить если есть такой челлендж и потом убирать


@message_handler.state('short_description')
def short_description(message: Message):
    new_challenge.short_description = message.text
    collection_users.update_one({"id": message.from_user.id},
                                {"$set": {"state": 'full_description'}})
    bot.send_message(message.chat.id, texts.full_description)


@message_handler.state('full_description')
def full_description(message: Message):
    new_challenge.full_description = message.text
    collection_users.update_one({"id": message.from_user.id},
                                {"$set": {"state": 'xp'}})
    bot.send_message(message.chat.id, texts.xp)


@message_handler.state('xp')
def xp(message: Message):
    if re.match(r'^[-+]?\d+$', message.text):
        new_challenge.xp = message.text
        collection_users.update_one({"id": message.from_user.id},
                                    {"$set": {"state": 'sp'}})
        bot.send_message(message.chat.id, texts.sp)
    else:
        bot.send_message(message.chat.id, "Please write a number")
        collection_users.update_one({"id": message.from_user.id},
                                    {"$set": {"state": 'xp'}})


@message_handler.state('sp')
def sp(message: Message):
    if re.match(r'^[-+]?\d+$', message.text):
        # bot.send_message(message.chat.id, "New challenge added", reply_markup=keyboards.admin_markup)
        new_challenge.sp = message.text
        # return_challenges()
        collection_users.update_one({"id": message.from_user.id},
                                    {"$set": {"state": 'goal'}})
        bot.send_message(message.chat.id, "Please write the index of the sport that you want to edit")
        bot.send_message(message.chat.id, texts.return_sports())
    else:
        bot.send_message(message.chat.id, "Please write a number")
        collection_users.update_one({"id": message.from_user.id},
                                    {"$set": {"state": 'sp'}})


@message_handler.state('goal')
def goal(message: Message):
    if re.match(r'^[-+]?\d+$', message.text):
        global st
        st = texts.sports[int(message.text) - 1]
        bot.send_message(message.chat.id, "Please write down how many hours you need to get in this sport")
        collection_users.update_one({"id": message.from_user.id},
                                    {"$set": {"state": 'goal_number'}})
    else:
        bot.send_message(message.chat.id, "Please write a number")
        collection_users.update_one({"id": message.from_user.id},
                                    {"$set": {"state": 'goal'}})


@message_handler.state('goal_number')
def goal(message: Message):
    if re.match(r'^[-+]?\d+$', message.text):
        new_challenge.goal[st] = int(message.text)
        bot.send_message(message.chat.id, texts.return_sports())
        bot.send_message(message.chat.id, "If you want to finish, click Finish or enter the sports index again",
                         reply_markup=keyboards.finish_markup)
        collection_users.update_one({"id": message.from_user.id},
                                    {"$set": {"state": 'goal'}})


    else:
        bot.send_message(message.chat.id, "Please write a number")
        collection_users.update_one({"id": message.from_user.id},
                                    {"$set": {"state": 'goal_number'}})
