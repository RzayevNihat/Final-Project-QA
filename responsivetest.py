from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Brauzer ayarları
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.implicitly_wait(5)
driver.get("https://www.reddit.com/")

# Fərqli ekran ölçüləri üçün funksiyalar
def test_responsive_view(width, height):
    print(f"\nTesting responsivlik üçün {width}x{height} ölçüləri.")
    driver.set_window_size(width, height)  # Pəncərə ölçüsünü təyin edir
    time.sleep(2)
    
# Responsivlik üçün ölçülər
responsive_sizes = [
    (1920, 1080),  # Desktop
    (1024, 768),   # Tablet
    (375, 812),    # Mobil (iPhone X ölçüsü)
]

# Responsivlik Testi
for size in responsive_sizes:
    test_responsive_view(size[0], size[1])


# Brauzeri bağla
time.sleep(3)
driver.quit()