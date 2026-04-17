import smtplib
import datetime as dt
import random
from pathlib import Path

MY_EMAIL = 'name@gmail.com'
PASSWORD = 'aaaaaaa'

# for password:
# go to this url
# https://myaccount.google.com/apppasswords
# login with your gmail account
# create app, copy passowrd which is shown on screen, paste in the value of password variable

now = dt.datetime.now()
# print(now.weekday())

def monday_quote():
    global MY_EMAIL, PASSWORD
    file_path = Path(__file__).parent.joinpath('quotes.txt')
    with open(file_path, 'r') as quotes:
        quotes_list = quotes.read().splitlines()
    
    quote = random.choice(quotes_list)
    subject = "Knock Knock - It's Monday Quote"
    target_mail = 'name@gmail.com'

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr = MY_EMAIL,
                            to_addrs = target_mail,
                            msg=f"Subject:{subject}\n\n{quote}")

if now.weekday() == 0: # Monday is 0 and Sunday is 6
    monday_quote()