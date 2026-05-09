from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

PRACTICE_URL = 'https://appbrewery.github.io/instant_pot/'
LIVE_URL = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
 
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7,ur;q=0.6", 
    "Priority": "u=0, i", 
    "Sec-Ch-Ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"Windows\"", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36", 
  }

response = requests.get(url=LIVE_URL, headers=headers)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

title_broken = soup.find(id='productTitle').text.split()
title = ' '.join(title_broken)

price = soup.find(class_='a-offscreen')
price = float(price.text.replace('IDR', '').replace(',',''))

BUY_PRICE = 1500000

if price < BUY_PRICE:
    subject = "Amazon Price Alert!!!"
    message = f"{title}\nPrice: IDR {price}\n{LIVE_URL}"
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr = MY_EMAIL,
                            to_addrs = RECIPIENT_EMAIL,
                            msg=f"Subject:{subject}\n\n{message}".encode('utf-8')
                            )
        print('--EMAIL SENT--')