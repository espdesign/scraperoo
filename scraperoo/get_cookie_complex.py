from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def get_cookies_complex(term_search):
    # Optional: set up Chrome options

    options = Options()
    options.add_argument("--headless")  # Uncomment to run without GUI

    # Initialize driver and wait
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    # Open the URL
    driver.get(
        "https://banweb.canton.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search"
    )

    # Wait for and click the dropdown trigger
    dropdown_trigger = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "select2-choice"))
    )
    dropdown_trigger.click()

    # Wait for the input field and enter the term
    search_input = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "select2-input"))
    )
    search_input.send_keys(f"{term_search}")
    time.sleep(1)  # Let results populate
    search_input.send_keys(Keys.ENTER)

    # Wait for and click the Continue button
    continue_button = wait.until(EC.element_to_be_clickable((By.ID, "term-go")))
    continue_button.click()

    search_button = wait.until(EC.element_to_be_clickable((By.ID, "search-go")))
    search_button.click()

    cookies = driver.get_cookies()
    for cookie in cookies:
        if len(cookie["value"]) == len("1F3635F8B5300845AD6ACF4448A84F73"):
            print("Cookie grabbed....", cookie["value"])
            return cookie["value"]
        



