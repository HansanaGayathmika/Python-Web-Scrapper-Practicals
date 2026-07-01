from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ✅ anti-detection options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

service = Service(
    executable_path="C:\\Users\\Hansana\\Desktop\\web_scrapper\\chromedriver.exe"
)

driver = webdriver.Chrome(service=service, options=options)  # ✅ pass options

# ✅ hide webdriver property
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)  # ✅ give Cloudflare time to verify

wait = WebDriverWait(driver, 15)

# Step 1: click language
lang_button = wait.until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
)
lang_button.click()

# Step 2: wait for cookie
cookie = wait.until(
    EC.element_to_be_clickable((By.ID, "bigCookie"))
)

# Step 3: click cookie many times
for i in range(100):  # click 100 times
    cookie.click()

print("Done clicking!")
driver.quit()
