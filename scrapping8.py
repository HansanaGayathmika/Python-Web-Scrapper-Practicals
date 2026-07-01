from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# ✅ add these options to hide bot detection
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

service = Service(
    executable_path="C:\\Users\\Hansana\\Desktop\\web_scrapper\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)  # ✅ pass options

# ✅ hide webdriver property using JavaScript
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://google.com")

input_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
input_element.send_keys("Youtube", Keys.ENTER)

input_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "YouTube"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "YouTube")
link.click()

time.sleep(5)
driver.quit()
