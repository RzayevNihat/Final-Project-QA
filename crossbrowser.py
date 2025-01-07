import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RedditLoginTest:
    def __init__(self, browser, username, password, address):
        self.username = username
        self.password = password
        
        if browser == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
        elif browser == "edge":
            service = EdgeService(EdgeChromiumDriverManager().install())
            options = webdriver.EdgeOptions()
            self.driver = webdriver.Edge(service=service, options=options)
        else:
            raise ValueError("Düzgün brauzer adı daxil edin: 'chrome' və ya 'edge'")

        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(3)

    def login(self):
        """Reddit hesabına giriş edir."""
        try:
            # İstifadəçi adını daxil edin
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
            )
            username_field.send_keys(self.username)

            # Şifrəni daxil edin
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
            )
            password_field.send_keys(self.password)

            # Enter düyməsini basın
            password_field.send_keys(Keys.RETURN)

            # Girişin uğurla olub-olmamasını yoxlayın
            time.sleep(5)
            print("Giriş testi tamamlandı.")
        except Exception as e:
            print("Giriş zamanı problem yarandı:", e)
        finally:
            self.driver.quit()

# Test data YAML faylını oxumaq
def load_test_data(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Test nümunəsi
if __name__ == "__main__":
    # Test məlumatlarını yükləyin
    testdata = load_test_data('testdata.yaml')
    browser = testdata["browser"]
    username = testdata["username"]
    password = testdata["password"]
    address = testdata["address"]

    print(f"\n{browser.upper()} ilə giriş testi başlanır...")
    reddit_test = RedditLoginTest(browser, username, password, address)
    reddit_test.login()
