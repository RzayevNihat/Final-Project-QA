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
    
    try:
        # Menü açılıb-açılmadığını yoxla
        menu_button = driver.find_element(By.XPATH, '//button[@aria-label="Open navigation"]')
        menu_button.click()
        print(f"{width}x{height} üçün menyu düyməsi görünür və işləyir.")
        time.sleep(2)
    except Exception as e:
        print(f"{width}x{height} ölçüsündə menyu düyməsi tapılmadı: {e}")

    # Popular düyməsini yoxla
    try:
        popular_button = driver.find_element(By.LINK_TEXT, "Popular")
        popular_button.click()
        print(f"{width}x{height} üçün 'Popular' düyməsi işləyir.")
        time.sleep(2)
    except Exception as e:
        print(f"{width}x{height} ölçüsündə 'Popular' düyməsi tapılmadı: {e}")

# Responsivlik üçün ölçülər
responsive_sizes = [
    (1920, 1080),  # Desktop
    (1024, 768),   # Tablet
    (375, 812),    # Mobil (iPhone X ölçüsü)
]

# Responsivlik Testi
for size in responsive_sizes:
    test_responsive_view(size[0], size[1])

# Log Out
try:
    profile_menu = driver.find_element(By.XPATH, '//*[@id="expand-user-drawer-button"]')
    profile_menu.click()
    time.sleep(2)
    
    logout_button = driver.find_element(By.XPATH, '//*[@id="logout-list-item"]/div')
    logout_button.click()
    print("Çıxış uğurla tamamlandı.")
except Exception as e:
    print(f"Çıxış zamanı problem: {e}")

# Brauzeri bağla
time.sleep(3)
driver.quit()
