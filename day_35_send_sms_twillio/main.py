import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

WEATHERMAP_API_KEY=os.getenv("WEATHERMAP_API_KEY")
ACCOUNT_SID=os.getenv("ACCOUNT_SID")
AUTH_TOKEN=os.getenv("AUTH_TOKEN")
PHONE_NUMBER=os.getenv("PHONE_NUMBER")
TWILLIO_WA_NUMBER=os.getenv("TWILLIO_WA_NUMBER")

parameters = {
    "lat": 44.583288,
    "lon": 146.949813,
    "cnt": 4,
    "appid": WEATHERMAP_API_KEY
}

response = requests.get(url=OMW_Endpoint, params=parameters)
response.raise_for_status()
# print(response.status_code)
weather_data = response.json()

# print(data)
# print(data['list'])
id_list = [hour_data["weather"][0]["id"] for hour_data in weather_data['list']]
print(id_list)

will_rain = False
for i in id_list:
    if i < 700:
        will_rain = True

if will_rain:
    # print("It's going to rain today. Remember to bring an ☔")
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        from_=f"whatsapp:{TWILLIO_WA_NUMBER}",
        body="It's going to rain today. Remember to bring an umbrella",
        to=f"whatsapp:{PHONE_NUMBER}"
    )

    print(message.status)
