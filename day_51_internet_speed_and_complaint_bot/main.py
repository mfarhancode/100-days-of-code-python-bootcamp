import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv('TWITTER_EMAIL')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')
Y_EMAIL = os.getenv('Y_EMAIL')
Y_PASSWORD = os.getenv('Y_PASSWORD')
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 3)
        self.down = 0
        self.up = 0

    def login_y(self):
        self.driver.get(Y_LOGIN_URL)
        wait = WebDriverWait(self.driver, 3)
        wait.until(ec.presence_of_element_located((By.NAME, "email")))
        email_input = self.driver.find_element(By.NAME, 'email')
        email_input.clear()
        email_input.send_keys(Y_EMAIL)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(Y_PASSWORD)
        login_btn = self.driver.find_element(By.CSS_SELECTOR, "button.y-login-submit")
        login_btn.click()
    
    # def login_twitter(self):
    #     self.driver.get('https://x.com/')
    #     wait = WebDriverWait(self.driver, 2)
    #     wait.until(ec.presence_of_element_located((By.NAME, "username_or_email")))
    #     email_input = self.driver.find_element(By.NAME, 'username_or_email')
    #     email_input.clear()
    #     email_input.send_keys(TWITTER_EMAIL)
    #     email_input.send_keys(Keys.ENTER)

        # We’ve temporarily limited your login. Please try again later.

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".start-text")))
        start_btn = self.driver.find_element(By.CSS_SELECTOR, '.start-text')
        start_btn.click()
        
        time.sleep(60)

        self.down = self.driver.find_element(By.CSS_SELECTOR, '.download-speed').text
        self.up = self.driver.find_element(By.CSS_SELECTOR, '.upload-speed').text

    def tweet_at_provider(self):
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 150down/10up?"
        tweet_box = self.driver.find_element(By.CSS_SELECTOR, '#tweet-compose')
        tweet_box.clear()
        tweet_box.send_keys(tweet)

        post_btn = self.driver.find_element(By.CSS_SELECTOR, '#post-btn')
        post_btn.click()


    
bot = InternetSpeedTwitterBot()

print('Testing internet speed...')
bot.get_internet_speed()
print('Downolad Speed:', bot.down)
print('Upload Speed:', bot.up)
print('Starting logging in...')
bot.login_y()
print('Logged in. Now it is time to post.')
bot.tweet_at_provider()
print('COMPLAIN POSTED!!')
