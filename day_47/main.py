from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")


PRACTICE_URL = 'https://appbrewery.github.io/instant_pot/'
LIVE_URL = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
 
response = requests.get(url=LIVE_URL)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

price = soup.find(class_='a-offscreen')
print(price)
price = price.text[1:]
print(price)
