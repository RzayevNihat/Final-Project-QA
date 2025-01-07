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

class RedditCrossBrowserTest:
    def __init__(self, browser):
        self.browser = browser
        if browser == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
        elif browser == "edge":
            service = EdgeService(EdgeChromiumDriverManager().install())
            self.driver = webdriver.Edge(service=service)
        else:
            raise ValueError("Düzgün brauzer adı daxil edin: 'chrome' və ya 'edge'.")

    def test_login(self):
        self.driver.get("https://www.reddit.com/login/")
        time.sleep(3)

        # İstifadəçi adı və şifrəni daxil edin
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
        )
        username_field.send_keys("nihat.rzayev1357@gmail.com")

        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
        )
        password_field.send_keys("salam1234salam")
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)
        print(f"{self.browser} ilə giriş testi tamamlandı.")

    def test_navigation(self):
        self.driver.get("https://www.reddit.com/")
        time.sleep(3)

        # 'Popular' bölməsinə keçin
        try:
            popular_link = WebDriverWait(self.driver, 15).until(  # Gözləmə müddətini artırdım
                EC.element_to_be_clickable((By.LINK_TEXT, "Popular"))
            )
            popular_link.click()
            time.sleep(5)
            print(f"{self.browser} ilə navigasiya testi tamamlandı.")
        except Exception as e:
            print(f"{self.browser} ilə navigasiya zamanı problem: {e}")




    def test_search(self):
        self.driver.get("https://www.reddit.com/")
        time.sleep(3)

        # Axtarış qutusuna "Python" yazın
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search Reddit']"))
            )
            search_box.send_keys("Python")
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)
            print(f"{self.browser} ilə axtarış testi tamamlandı.")
        except Exception as e:
            print(f"{self.browser} ilə axtarış zamanı problem: {e}")

    def quit(self):
        self.driver.quit()

# Test nümunəsi
if __name__ == "__main__":
    browsers = ["chrome", "edge"]  # Test üçün brauzer siyahısı

    for browser in browsers:
        print(f"\n{browser.upper()} ilə Reddit testi başlanır...")
        reddit_test = RedditCrossBrowserTest(browser)
        reddit_test.test_login()
        reddit_test.test_navigation()
        reddit_test.test_search()
        reddit_test.quit()
