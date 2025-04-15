from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://banweb.canton.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search")

title = driver.title

driver.implicitly_wait(0.5)

submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit()