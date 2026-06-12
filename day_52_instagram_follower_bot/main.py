from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ec
import time


load_dotenv()

IG_USERNAME = os.getenv('IG_USERNAME')
PASSWORD = os.getenv('PASSWORD')  
SIMILAR_ACCOUNT = "hiking_aesthetics"   # the account whose followers you'll follow
URL = "https://www.instagram.com"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 3)

    def login(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 3)
        wait.until(ec.presence_of_element_located((By.NAME, "email")))
        email_input = self.driver.find_element(By.NAME, 'email')
        email_input.clear()
        email_input.send_keys(IG_USERNAME)
        password_input = self.driver.find_element(By.NAME, 'pass')
        password_input.clear()
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(4)


    def find_followers(self):
        self.driver.get(f"{URL}/{SIMILAR_ACCOUNT}")
        time.sleep(2)
        followers_link = self.driver.find_element(By.XPATH, "//*[contains(text(), 'followers')]")
        followers_link.click()
        time.sleep(2)
        scroll = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        
        for i in range(50):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            time.sleep(3)

    def follow(self):
        list_follow_btns = self.driver.find_elements(By.CSS_SELECTOR, "._aswp._aswr._aswu._asw_._asx2")
        for btn in list_follow_btns:
            # self.driver.execute_script("arguments[0].click();", btn)
            try:
                self.driver.execute_script("arguments[0].click();", btn)
                time.sleep(3)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                self.driver.execute_script("arguments[0].click();", cancel_button)
            


    
ig_bot = InstaFollower()
ig_bot.login()
ig_bot.find_followers()
ig_bot.follow()