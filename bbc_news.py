from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import schedule


def scrape_news():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/news")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "h2[data-testid='card-headline']"))
    )

    time.sleep(2)

    with open(r"C:\\Users\\Hansana\\Desktop\\web_scrapper\\bbc_news.txt", "a", encoding="utf-8")as file:

        doc = BeautifulSoup(driver.page_source, 'html.parser')

        headlines = doc.find_all("h2", attrs={"data-testid": "card-headline"})

        for headline in headlines:
            file.write(f"{headline.text.strip()}\n")
            file.write("\n")

        driver.quit()
        print("Scraped Successfully.")


schedule.every(1).hour.do(scrape_news)

while True:
    schedule.run_pending()
    time.sleep(1)
