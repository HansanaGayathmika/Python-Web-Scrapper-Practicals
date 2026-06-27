from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"

page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

quotes = doc.find_all(class_="quote")

for quote in quotes:
    text = quote.find('span').string
    author = quote.find(class_="author").string

    print(text)
    print(author)
    tags = quote.find_all("a", class_="tag")
    for tag in tags:
        print(tag.text)
    print()
