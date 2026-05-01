import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.environ['MY_EMAIL']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
RECEIVER_EMAIL = os.environ['RECEIVER_EMAIL']


class NotificationManager:

    def __init__(self):
        self.my_email = MY_EMAIL
        self.email_password = EMAIL_PASSWORD
        self.receiver_email = RECEIVER_EMAIL

    # def send_email(self, subject, body):
    #     message = f"Subject:{subject}\n\n{body}"
    #
    #     with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    #         connection.starttls()
    #         connection.login(user=self.my_email, password=self.email_password)
    #         connection.sendmail(
    #                             from_addr=self.my_email,
    #                             to_addrs=self.receiver_email,
    #                             msg=message.encode("utf-8")
    #                             )
    def send_emails(self, subject, body, email_list):
        message = f"Subject:{subject}\n\n{body}"

        for email in email_list:
            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.email_password)
                connection.sendmail(
                                    from_addr=self.my_email,
                                    to_addrs=email,
                                    msg=message.encode("utf-8")
                                    )
