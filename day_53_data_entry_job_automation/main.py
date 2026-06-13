from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ec
import time

GOOGLE_FORM = ""

response = requests.get('https://appbrewery.github.io/Zillow-Clone/')

zillow_webpage = response.text

soup = BeautifulSoup(zillow_webpage, 'html.parser')

listings = soup.select('[class^="ListItem"]')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


for listing in listings:
    driver.get(GOOGLE_FORM)
    time.sleep(1)
    link = listing.find(class_='property-card-link').get('href')
    
    price = listing.find(class_='PropertyCardWrapper__StyledPriceLine').getText()
    if '+' in price:
        price, _ = price.split('+')
    else:
        price, _ = price.split('/')

    address = listing.find('address').getText().strip().replace(' | ', ' ')

    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address)

    price_input = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price)

    link_input = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(link)

    submit_btn = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_btn.click()
    time.sleep(2)
