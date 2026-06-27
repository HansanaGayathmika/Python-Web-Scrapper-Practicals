from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"

page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

quotes = doc.find_all(class_="quote")

with open(r"C:\Users\Hansana\Desktop\web_scrapper\quotes.csv", "w")as file:
    for quote in quotes:
        text = quote.find('span').string
        author = quote.find(class_="author").string
        file.write(f"{text}\n")
        file.write(f"{author}\n")
        tags = quote.find_all("a", class_="tag")
        for tag in tags:
            file.write(f"{tag.text}\n")
