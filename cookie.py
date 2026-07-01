import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = uc.Chrome()  # ✅ automatically bypasses Cloudflare
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)

wait = WebDriverWait(driver, 15)

lang_button = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
lang_button.click()

cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))

for i in range(100):
    cookie.click()

print("Done!")
driver.quit()
