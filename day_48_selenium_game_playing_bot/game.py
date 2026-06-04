from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep, time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://ozh.github.io/cookieclicker/')

sleep(3)

try:
    eng = driver.find_element(By.CSS_SELECTOR, value='#langSelect-EN')
    eng.click()
except NoSuchElementException:
    print("Language selection not found")

sleep(2)
cookie = driver.find_element(By.CSS_SELECTOR, value='#bigCookie')


wait_time = 20
timeout = time() + wait_time  # Check for purchases every 5 seconds
five_min = time() + 60 * 5  # Run for 5 minutes

while True:
    cookie.click()
    if time() > timeout:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", "")) 
            
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")   

            best_item = None
            for product in reversed(products):  # Start from most expensive (bottom of list)
                # Check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break
            
            if best_item:
                try:
                    best_item.click()
                    best_item_id = best_item.get_attribute('id')
                    best_item_name = driver.find_element(By.CSS_SELECTOR, value=f'#{best_item_id}')
                    print(f"Bought item : {best_item_name.text.split()[0]}")
                except ElementClickInterceptedException:
                    print("Click was intercepted, trying to remove any banners and retry...")
                    try:
                        banner = driver.find_element(By.CLASS_NAME, "cc_banner")
                        driver.execute_script("arguments[0].remove();", banner)
                        best_item.click()
                        best_item_id = best_item.get_attribute('id')
                        best_item_name = driver.find_element(By.CSS_SELECTOR, value=f'#{best_item_id}')
                        print(f"Bought item : {best_item_name.text.split()[0]}")
                    except Exception as e:
                        print("Still couldn't click item:", e)
                
                
        except (NoSuchElementException, ValueError):
                print("Couldn't find cookie count or items")
            
        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break


sleep(5)
driver.quit()