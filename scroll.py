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

time.sleep(10)

scroll_page=0

for i in range(3):
    scroll_page+=660
    driver.execute_script(f"window.scrollTo(0, {scroll_page});")
    time.sleep(3) 

profile_menu = driver.find_element(By.XPATH, '//*[@id="expand-user-drawer-button"]')
profile_menu.click()

time.sleep(2)

logout_button = driver.find_element(By.XPATH, '//*[@id="logout-list-item"]/div')
logout_button.click()
time.sleep(5)
driver.quit()