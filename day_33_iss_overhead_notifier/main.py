import requests
from datetime import datetime
import pytz
import smtplib
import time
import os
from dotenv import load_dotenv

load_dotenv()

MY_LAT = os.getenv("MY_LAT") # Your latitude
MY_LONG = os.getenv("MY_LONG") # Your longitude

MY_EMAIL = os.getenv("MY_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# print(sunset, sunrise)

jakarta_tz = pytz.timezone('Asia/Jakarta')
time_now = datetime.now(jakarta_tz)


hour = time_now.hour
# print(hour)

#If the ISS is close to my current position

def is_iss_near():
    global MY_LAT, MY_LONG
    resp = requests.get(url='http://api.open-notify.org/iss-now.json')
    resp.raise_for_status()
    data_iss = resp.json()
    longitude = float(data_iss['iss_position']['longitude'])
    latitude = float(data_iss['iss_position']['latitude'])
    iss_position = (longitude, latitude)
    # print(iss_position)
    if (MY_LONG + 5) >= longitude >= (MY_LONG - 5) and (MY_LAT + 5) >= latitude >= (MY_LAT - 5):
        return True

    return False

# print(is_iss_near())

# and it is currently dark
def is_dark():
    global hour, sunset, sunrise
    if hour >= sunset or hour <= sunrise:
        return True
    return False

def main():
    print("Checking ISS position and sky conditions...")
    if is_dark() and is_iss_near():
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=RECIPIENT_EMAIL,
                                msg="Subject:Look Up\n\nISS is over you!!!")
        print("Email notification sent!")


while True:
    main()
    time.sleep(60)