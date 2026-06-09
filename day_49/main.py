from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import sys

ACCOUNT_EMAIL = "name@test.com" 
ACCOUNT_PASSWORD = "password"    
GYM_URL = "https://appbrewery.github.io/gym/"
BOOKING_TIME = '6:00 PM'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = Path(__file__).parent.joinpath("chrome_profile")
# print(user_data_dir)

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)
login_page_btn = driver.find_element(By.CSS_SELECTOR, value= '.Home_heroButton__3eeI3')
login_page_btn.click()


def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)


def login():
    wait.until(ec.presence_of_element_located((By.ID, "login-page")))

    email_entry = driver.find_element(By.NAME, value= 'email')
    email_entry.clear()
    email_entry.send_keys(ACCOUNT_EMAIL)

    password_entry = driver.find_element(By.NAME, value= 'password')
    password_entry.clear()
    password_entry.send_keys(ACCOUNT_PASSWORD)


    submit_btn = driver.find_element(By.CSS_SELECTOR, value= '#submit-button')
    submit_btn.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

retry(login, description="login")
print('Successfully Logged In')

def book_classes():
    global classes_booked, classes_waitlisted, already_booked_waitlisted, processed_classes
    class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

    classes_booked = 0
    classes_waitlisted = 0
    already_booked_waitlisted = 0

    processed_classes = []

    for card in class_cards:
        day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group')]")
        day_title = day_group.find_element(By.TAG_NAME, "h2").text

        if 'Tue' in day_title or 'Thu' in day_title:
            time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

            if BOOKING_TIME in time_text:
                class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
                button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
                btn_txt = button.text.lower()
                class_info = f"{class_name} on {day_title}"
                
                if btn_txt == 'booked':
                    already_booked_waitlisted += 1
                    print(f"✓ Already Booked: {class_info}")
                    processed_classes.append(f"[Booked] {class_info}")
                elif btn_txt == 'waitlisted':
                    already_booked_waitlisted += 1
                    print(f"✓ Already on waitlist for: {class_info}")
                    processed_classes.append(f"[Waitlisted] {class_info}")
                elif btn_txt == 'join waitlist':
                    def join_waitlist(retries, button):
                        global processed_classes, classes_waitlisted
                        if retries == 0:
                            return
                        print('Trying to join waitlist. Attempt ', abs(retries-8))
                        button.click()
                        
                        time.sleep(2)
                        after_button_text = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']").text.lower()
                        
                        if btn_txt == after_button_text:
                            retries -= 1
                            join_waitlist(retries, button)
                        else:
                            print(f"✓ Joined waitlist for: {class_info}")
                            processed_classes.append(f"[New Waitlist] {class_info}")
                            classes_waitlisted += 1
                            return
                    join_waitlist(7, button)

                elif btn_txt == 'book class':
                    def book_class(retries, button):
                        global processed_classes, classes_booked
                        if retries == 0:
                            return
                        print('Trying booking. Attempt ', abs(retries-8))
                        button.click()
                        
                        time.sleep(2)
                        after_button_text = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']").text.lower()
                        print(btn_txt, after_button_text)
                        if btn_txt == after_button_text:
                            retries -= 1
                            book_class(retries, button)
                        else:
                            classes_booked += 1
                            print(f"✓ Successfully Booked: {class_info}")
                            processed_classes.append(f"[New Booking] {class_info}")
                            return
                    book_class(7, button)

                
retry(book_classes, description="Booking classes")

# print(f"""
# --- BOOKING SUMMARY ---
# Classes booked: {classes_booked}
# Waitlists joined: {classes_waitlisted}
# Already booked/waitlisted: {already_booked_waitlisted}
# Total Tuesday 6pm classes processed: {classes_booked + classes_waitlisted + already_booked_waitlisted}
# """)

# print("--- DETAILED CLASS LIST ---")
# print(details)


total_booked = classes_booked + classes_waitlisted + already_booked_waitlisted
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")


def verification():
    driver.get('https://appbrewery.github.io/gym/my-bookings/')
    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

    # print(bookings_counts, waitlist_counts)
    verified_count = 0
    all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
    for card in all_cards:
        try:
            when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
            when_text = when_paragraph.text

            # Check if it's a Tuesday or Thursday 6pm class
            if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
                class_name = card.find_element(By.TAG_NAME, "h3").text
                print(f"  ✓ Verified: {class_name}")
                verified_count += 1
        except NoSuchElementException:
            # Skip if no "When:" text found (not a booking card)
            pass

    # Simple comparison
    print(f"\n--- VERIFICATION RESULT ---")
    print(f"Expected: {total_booked} bookings")
    print(f"Found: {verified_count} bookings")

    if total_booked == verified_count:
        print("✅ SUCCESS: All bookings verified!")
    else:
        print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")
        
retry(verification, description="Verification")