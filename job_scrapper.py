from bs4 import BeautifulSoup
from scrapping8 import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import re

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://remoteok.com/")

# ✅ correct way to wait for job rows
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "tr[data-offset]"))
)

time.sleep(2)  # extra wait to load all jobs

doc = BeautifulSoup(driver.page_source, 'html.parser')
job_titles = doc.find_all("tr", attrs={"data-offset": True})

for job in job_titles:

    tags = job.find_all(class_="tag")
    tag_names = [tag.text.strip().lower() for tag in tags]

    if not re.search(r"python", tag_names, re.IGNORECASE):
        continue
    title = job.find('h2').text.strip()
    company = job.find('h3').text.strip()
    salary_tag = job.find(class_="salary")
    if salary_tag:
        salary = salary_tag.text.strip()
    else:
        salary = "Salary not available"

    print(title)
    print(company)
    print(salary)
    print("-"*20)

driver.quit()
