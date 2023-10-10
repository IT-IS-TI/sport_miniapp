import unittest
from datetime import datetime
import telebot
from telebot import types


class TestBot(unittest.TestCase):
    def setUp(self):
        # Setting up test data
        self.bot = telebot.TeleBot('6155094584:AAE5isPBEmZ1quEGKICR2h5y7bZ9YGhN2sM')
    def tearDown(self):
        # Cleaning after each test
        self.bot = None

    def test_start_handler(self):
        # Testing the "/start" button handler

        # Preparing test data
        user = types.User(id=67890, is_bot=False, first_name='John')
        chat = types.Chat(id=123, type='public')  # Замените 'private' на нужный тип чата
        message = types.Message(
            message_id=84765,
            from_user=user,
            date=datetime.now(),
            chat=chat,
            content_type='text',
            options={},
            json_string=''
        )
        message.text = '/start'

        # Calling the "/start" button handler
        self.bot.process_new_messages([message])

        # Check connection and rendering


    def test_about_handler(self):
        # Testing the "About" button handler

        # Preparing test data
        user = types.User(id=67890, is_bot=False, first_name='Bob')
        chat = types.Chat(id=123, type='public')  # Замените 'private' на нужный тип чата
        message = types.Message(
            message_id=423123,
            from_user=user,
            date=datetime.now(),
            chat=chat,
            content_type='text',
            options={},
            json_string=''
        )
        message.text = 'About'

        # Calling the "About" button handler
        self.bot.process_new_messages([message])

        # Check connection and rendering

