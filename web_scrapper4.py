from scrapping8 import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://coinmarketcap.com/")

html = driver.page_source
doc = BeautifulSoup(html, "html.parser")

tbody = doc.find("tbody")
trs = tbody.contents
print(list(trs[0].descendants))
