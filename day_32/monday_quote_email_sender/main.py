# import smtplib
# import datetime as dt
# import random
# from pathlib import Path

# MY_EMAIL = 'name@gmail.com'
# PASSWORD = 'aaaaaaa'

# # for password:
# # go to this url
# # https://myaccount.google.com/apppasswords
# # login with your gmail account
# # create app, copy passowrd which is shown on screen, paste in the value of password variable

# now = dt.datetime.now()
# # print(now.weekday())

# def monday_quote():
#     global MY_EMAIL, PASSWORD
#     file_path = Path(__file__).parent.joinpath('quotes.txt')
#     with open(file_path, 'r') as quotes:
#         quotes_list = quotes.read().splitlines()
    
#     quote = random.choice(quotes_list)
#     subject = "Knock Knock - It's Monday Quote"
#     target_mail = 'name@gmail.com'

#     with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(from_addr = MY_EMAIL,
#                             to_addrs = target_mail,
#                             msg=f"Subject:{subject}\n\n{quote}")

# if now.weekday() == 0: # Monday is 0 and Sunday is 6
#     monday_quote()

# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

# import os and use it to get the Github repository secrets


import smtplib
import datetime as dt
import random
from pathlib import Path
import os

MY_EMAIL = "bapakfarhan1212@gmail.com"
MY_PASSWORD = "rouqaxnkvdvepeaz"
RECIPIENT_EMAIL = "fani8731507@gmail.com"

# for password:
# go to this url
# https://myaccount.google.com/apppasswords
# login with your gmail account
# create app, copy passowrd which is shown on screen, paste in the value of password variable

# now = dt.datetime.now()
# print(now.weekday())

def daily_quote():
    global MY_EMAIL, MY_PASSWORD
    file_path = Path(__file__).parent.joinpath('quotes.txt')
    with open(file_path, 'r') as quotes:
        quotes_list = quotes.read().splitlines()
    
    quote = random.choice(quotes_list)
    subject = "Knock Knock - It's Daily Quote"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr = MY_EMAIL,
                            to_addrs = RECIPIENT_EMAIL,
                            msg=f"Subject:{subject}\n\n{quote}")

if __name__ == "__main__":
    daily_quote()

