from telebot.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, \
    ReplyKeyboardRemove, WebAppInfo
from datetime import date, timedelta
from user import User
from answers.texts import emoji

default_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
buttonAbout = KeyboardButton("About")
buttonHelp = KeyboardButton("Help")
buttonSettings = KeyboardButton("Settings")
buttonAuthorize = KeyboardButton("Sign in")
default_markup.add(buttonAbout, buttonHelp, buttonAuthorize)

default_markup2 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

# webAppTest = WebAppInfo("https://lambent-sorbet-1fcf63.netlify.app")
InlineProfile = InlineKeyboardButton("Profile",
                                     web_app=WebAppInfo(url="https://lambent-sorbet-1fcf63.netlify.app"))
# InlineProfile = InlineKeyboardButton("", web_app="https://lambent-sorbet-1fcf63.netlify.app")


buttonProfile = KeyboardButton(text="Profile")

default_markup2.add(buttonAbout, buttonHelp, buttonProfile)
Profile_markup = InlineKeyboardMarkup(row_width=1)
Profile_markup.add(InlineProfile)

admin_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
buttonChallanges = KeyboardButton("Challenges")
admin_markup.add(buttonAbout, buttonHelp, buttonProfile, buttonChallanges)
buttonView = InlineKeyboardButton("View", callback_data='View')
buttonAdd = InlineKeyboardButton("Add", callback_data='Add')
buttonDelete = InlineKeyboardButton("Delete", callback_data='Delete')

challenges_markup = InlineKeyboardMarkup(row_width=2)
challenges_markup.add(buttonView, buttonAdd, buttonDelete)



finish_markup = InlineKeyboardMarkup(row_width=1)
buttonFinish = InlineKeyboardButton('Finish', callback_data='Finish')
finish_markup.add(buttonFinish)


remove = ReplyKeyboardRemove()
