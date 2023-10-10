import challenges

emoji = {'correct': '\U00002705', 'wrong': '\U0000274C', 'back': '\U00002B05', 'hi': '\U0001F44B',
         't-shirt': '\U0001F455', 'bag': '\U0001F6CD', 'cap': '\U0001F9E2', 'photo': '\U0001F9B0', 'dice': '\U0001F3B2',
         'time': '\U000023F3', 'cup': '\U00002615', 'long sleeve': '\U0001F97C', 'food': '\U0001F372',
         'blocknote': '\U0001F4D2', }

greetings = '''
Welcome to InnoSportChallengesBot.
'''
login = '''
To register you on Innopolis Sport website, please write your Innopolis email.
The domain should be: innopolis.university or innopolis.ru
'''
About_Button = f'{emoji["hi"]}Hello! \nIt is a bot with sport challenges for Innopolis University’s students.\n ' \
               f'Here you can perform sports challenges, earn SportPoints for it and exchange them for merch.'

Help_Button = '''
🔗 Link to official Sport site:
sport.innopolis.university

💰 Sp (Sport points) - special currency for our app. You can earn it by completing official challenges. In the future it will be possible to convert sp into innopoints or University's merch

📈 Lvl and XP - you can earn XP by completing any challenges and higher up your lvl

🕐 Sport hours - equivalent to sport hours from official site (https://sport.innopolis.university/). They are updating every 4 hours.

💪 You want to create your own challenge? Write to our content manager: "telegram_username is hidden due to TG contest"

❓Have any technical issues or want to suggest new feature? Contact our tech guru - "telegram_username is hidden due to TG contest"
'''
Notification_Button = '''
Turn the Notifications ON or OFF ?
'''

On = f'{emoji["correct"]} ON'

Off = f'{emoji["wrong"]} OFF'

Notifications_On = 'Notifications are ON'

Notifications_Off = 'Notifications are OFF'

Back = 'Back'

Mistake = '''
Sorry, I don't understand you.
'''

password = '''
Please write your password.
'''
registered = '''
Your account has been successfully registered.
'''
already_registered = "Your account is already registered"

admin_password = '''
Please write admin's password.
'''

InnoStore = '''
You can exchange earned gems for merch from Innostore.
https://ipts.innopolis.university/products
'''

regirstation = '''
We register you...
'''

wrong_password = '''
Wrong password
'''
login_successful = '''
Login successful
'''

id = '''
Please write the "id" of the challenge
'''

name = '''
Please write the name of the challenge
'''
short_description = '''
Please write the short description of the challenge
'''
full_description = '''
Please write the long description of the challenge
'''
xp = '''
Please write how many Xp points the challenge will have
'''
sp = '''
Please write how many SportPoints(SP) points the challenge will have
'''

Sport_sessions = {
    "General Physical Training": 0.0,
    "Follow the Bars - Running": 0.0,
    "Social Dance": 0.0,
    "Functional LCD": 0.0,
    "RAGE": 0.0,
    "Boxing": 0.0,
    "Table tennis - Advanced": 0.0,
    "Volleyball": 0.0,
    "RAGE - Knights": 0.0,
    "Street Dance": 0.0,
    "Football": 0.0,
    "Sambo": 0.0,
    "Tricking club": 0.0,
    "Basketball": 0.0,
    "Yoga - Stretching": 0.0,
    "Tennis": 0.0,
    "Yoga - Strength": 0.0,
    "Badminton - Advanced": 0.0,
    "Badminton - Beginners": 0.0,
    "Mixed sports": 0.0,
    "Park Run - 5 Verst": 0.0,
    "Cricket": 0.0,
    "Extra sport events": 0.0
}
Profile = '''
Here you can see information about your challenges. You can track your progress, complete challenges and earn SportPoints.
'''

sports = [
    "General Physical Training",
    "Follow the Bars - Running",
    "Social Dance",
    "Functional LCD",
    "RAGE",
    "Boxing",
    "Table tennis - Advanced",
    "Volleyball",
    "RAGE - Knights",
    "Street Dance",
    "Football",
    "Sambo",
    "Tricking club",
    "Basketball",
    "Yoga - Stretching",
    "Tennis",
    "Yoga - Strength",
    "Badminton - Advanced",
    "Badminton - Beginners",
    "Mixed sports",
    "Park Run - 5 Verst",
    "Cricket",
    "Extra sport events",
    "Full hours"
]


def return_sports():
    x = ""
    ind = 1
    for i in sports:
        x += (str(ind) + ":" + i + "\n")
        ind += 1
    return x
