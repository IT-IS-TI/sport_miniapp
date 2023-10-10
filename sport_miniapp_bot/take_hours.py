from requests.exceptions import ContentDecodingError, ConnectionError, RetryError
from requests import session as create_request_session, get
from requests.sessions import Session
from bs4 import BeautifulSoup
from pymongo.mongo_client import MongoClient

SERVER_URL = 'https://sport.innopolis.university'


def is_dead() -> bool:
    return get(SERVER_URL).status_code != 200


def login_user(email: str, password: str) -> Session:
    s = create_request_session()
    res = s.get(f'{SERVER_URL}/oauth2/login')
    if res.status_code != 200:
        raise ConnectionError('Server is down')

    bs = BeautifulSoup(res.content, 'html.parser')
    oath_url = bs.find('form', {'id': 'options'}).get('action')
    res = s.post(oath_url, data={
        'UserName': email,
        'Password': password,
        'AuthMethod': 'FormsAuthenication'})
    bs = BeautifulSoup(res.content, 'html.parser')
    dif_error = bs.find('div', {'id': 'error'})
    if res.status_code != 200:
        raise RetryError('Authentication problem on the server side')
    if dif_error is not None:
        return 'Error'
    s.cookies['student_id'] = bs.find('div', {'class': 'card-body'}).find('script').text.split('\n')[1].split('"')[1]
    return s




def get_user_statistics(session: Session) -> dict:
    return {
        'final_hours':
            session.get(f'{SERVER_URL}/api/attendance/{session.cookies["student_id"]}/negative_hours').json()[
                'final_hours'],
        'better_than': session.get(f'{SERVER_URL}/api/attendance/{session.cookies["student_id"]}/better_than').json(),
        'partial_hours': session.get(f'{SERVER_URL}/api/profile/history_with_self/21').json()
    }


All_sport_sessions = {
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

client = MongoClient(
    'mongodb+srv://dbUser:sma0l2PoInACsFJx@cluster0.ujmws.mongodb.net/SportAchievements?retryWrites=true&w=majority')
db = client['SportAchievements']
collection_users = db['users']


def update(id):
    state = collection_users.find({"id": id})
    for doc in state:
        login = doc["login"]
        password = doc["password"]
        student_hours = All_sport_sessions
        session = login_user(login, password)
        if session == 'Error':
            return "Error"
        else:
            for i in get_user_statistics(session)["partial_hours"]["trainings"]:
                student_hours[i["group"]] += i["hours"]
            full_hours = sum(student_hours.values())
            collection_users.update_one({"id": doc["id"]}, {"$set": {"certain_hours": student_hours}})
            collection_users.update_one({"id": doc["id"]}, {"$set": {"full_hours": full_hours}})
