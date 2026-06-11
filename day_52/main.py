from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
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

        scroll = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        scroll = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
        for i in range(10):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            time.sleep(2)
            """
             _aswp _aswr _aswu _asw_ _asx2
             _aswp _aswr _aswu _asw_ _asx2
              _aswp _aswr _aswu _asw_ _asx2

            """
            list_btns = driver.find_elements(By.CSS_SELECTOR, "._aswp._aswr._aswu._asw_._asx2")
            for btn in list_btns:
                btn.click()
    
    def follow(self):
        pass


    
ig_bot = InstaFollower()
ig_bot.login()
ig_bot.find_followers()

