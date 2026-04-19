from datetime import datetime
import requests

# 51.489205, -0.074955
MY_LAT = 51.489205
MY_LNG = -0.074955

# MY_LAT = -7.129792
# MY_LNG = 112.738056

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get(url=' https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
# print(data)
sunrise = int(data['results']['sunrise'].split("T")[1].split(':')[0])
sunset = int(data['results']['sunset'].split("T")[1].split(':')[0])
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)