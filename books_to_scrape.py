from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com/"

page = requests.get(url).text
doc = BeautifulSoup(page, 'html.parser')

books = doc.find_all(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

for book in books:
    title = book.find('h3').text
    price = book.find(class_="price_color").text

    rating_tag = book.find("p", class_="star-rating")
    rating = rating_tag['class'][1]

    print(title)
    print(price)
    print(f"rating: {rating}")
    print("-" * 20)
