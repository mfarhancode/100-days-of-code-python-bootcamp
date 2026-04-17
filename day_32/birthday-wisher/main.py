import pandas
import datetime as dt
from random import choice
import smtplib
from pathlib import Path
import sys

MY_EMAIL = 'bapakfarhan1212@gmail.com'
PASSWORD = 'rouqaxnkvdvepeaz'


# for password:
# go to this url
# https://myaccount.google.com/apppasswords
# login with your gmail account
# create app, copy passowrd which is shown on screen, paste in the value of password variable


def pick_random_letter(name):
    letters_folder = Path(__file__).parent.joinpath('letter_templates')
    letter_path = choice(list(letters_folder.glob('*.txt')))
    # print(letters_path)
    # print(random_letter_path)
    return letter_path.read_text().replace('[NAME]', name)
    
    
# print(pick_random_letter('farhan'))

def send_birthday_email(name, recipient_email):
    letter = pick_random_letter(name)
    try:
        with smtplib.SMTP('smtp.gmail.com', port=587) as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=PASSWORD)
            conn.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=recipient_email,
                    msg=f"Subject:Happy Birthday\n\n{letter}"
                )
        print(f'Email sent to {name}, : {recipient_email}')
    except Exception as e:
        print(f'[ERROR] Failed to send an email to {name} : {recipient_email} \n {e}')
    

def main():
    today = dt.datetime.now()

    csv_path = Path(__file__).parent.joinpath('birthdays.csv')
    data = pandas.read_csv(csv_path)

    today_birthdays = data[(data['month'] == today.month) & (data['day'] == today.day)]
    # print(today_birthdays)

    if today_birthdays.empty:
        print('No birthdays today.')
        return

    for _, row in today_birthdays.iterrows():
        # print(row['name'], row['email'])
        send_birthday_email(row['name'], row['email'])


if __name__ == '__main__':
    main()