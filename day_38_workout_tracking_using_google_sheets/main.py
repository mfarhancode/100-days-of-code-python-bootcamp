import requests, os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

WEIGHT = 60
HEIGHT = 169
AGE = 20

PASSWORD = os.getenv("PASSWORD")

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
q = input('Tell me which exercises you did: ')
param = {
    'query' : q,
    'weight_kg' : WEIGHT,
    'height_cm' : HEIGHT,
    'age' : AGE
}
header = {
    'x-app-id' : APP_ID,
    'x-app-key' : API_KEY
}

response = requests.post(url=exercise_endpoint,json=param, headers=header)
result = response.json()
print(result)

sheet_endpoint = os.environ["sheet_endpoint"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:

    body = {
            'workout': {
                'date':today_date,
                'time':now_time,
                'exercise':exercise['name'].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
# print(body)

    sheet_response = requests.post(url=sheet_endpoint, json=body, auth=('fani', PASSWORD))
    print(sheet_response.status_code)
