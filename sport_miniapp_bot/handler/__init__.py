from telebot import types
from user import User, collection_users


class Handler:
    def __init__(self):
        self.__handlers = {}

    def handle(self, message: types.Message):
        user_id = message.from_user.id
        user_db = collection_users.find_one({'id': user_id})
        if user_db == None:
            new_user = User(user_id)
            collection_users.insert_one(vars(new_user))
        state = collection_users.find_one({'id': user_id})["state"]
        args = []
        if state[-1] == ')':
            args = state[state.rfind('(') + 1:-1].split(',')
            state = state[:state.rfind('(')]
        if state in self.__handlers:
            self.__handlers[state](message, *args)

    def state(self, name: str):
        def decorator(func):
            self.__handlers[name] = func

        return decorator


message_handler = Handler()
callback_query_handler = Handler()

from . import message_handles
from . import callback_handles
