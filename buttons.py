from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.implicitly_wait(5)
driver.get("https://www.reddit.com/")

# Log in
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys("Several_Accident106")
password_input.send_keys("salam1234salam")
login_button2 = driver.find_element(By.XPATH, '//*[@id="login"]/auth-flow-modal/div[2]/faceplate-tracker/button')
login_button2.click()

# Wait for the page to load
time.sleep(10)

message_button = driver.find_element(By.XPATH, '//*[@id="header-action-item-chat-button"]')
message_button.click()
time.sleep(5)
message_button.click()
time.sleep(5)

notification_button = driver.find_element(By.XPATH, '//*[@id="mini-inbox-tooltip"]/span/faceplate-tracker/faceplate-tooltip/button')
notification_button.click()
time.sleep(5)
notification_button.click()
time.sleep(5)

profile_menu = driver.find_element(By.XPATH, '//*[@id="expand-user-drawer-button"]')
profile_menu.click()
time.sleep(2)

settings_button = driver.find_element(By.XPATH, '//*[@id="user-drawer-content"]/ul[3]/faceplate-tracker/li/a')
settings_button.click()
time.sleep(5)
homepage=driver.find_element(By.XPATH, '//*[@id="reddit-logo"]')
homepage.click()
time.sleep(5)

profile_menu = driver.find_element(By.XPATH, '//*[@id="expand-user-drawer-button"]')
profile_menu.click()
time.sleep(2)

achievement_button = driver.find_element(By.XPATH, '//*[@id="user-drawer-content"]/ul[1]/faceplate-tracker[3]/li/a')
achievement_button.click()
time.sleep(5)

profile_menu = driver.find_element(By.XPATH, '//*[@id="expand-user-drawer-button"]')
profile_menu.click()
time.sleep(2)

darkmode=driver.find_element(By.XPATH, '//*[@id="darkmode-list-item"]/div/span[2]/span/faceplate-switch-input')
darkmode.click()
time.sleep(5)
darkmode.click()
time.sleep(5)
# Click on the "Log out" button
logout_button = driver.find_element(By.XPATH, '//*[@id="logout-list-item"]/div')
logout_button.click()

# Wait for logout to complete
time.sleep(5)

# Close the browser
driver.quit()