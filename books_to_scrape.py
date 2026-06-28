from bs4 import BeautifulSoup
import requests

base_url = "http://books.toscrape.com/"
url = "/"

with open(r"C:\\Users\\Hansana\\Desktop\\web_scrapper\\books.csv", "w", encoding="utf-8")as file:
    while url:
        page = requests.get(base_url + url).text
        doc = BeautifulSoup(page, 'html.parser')
        books = doc.find_all(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        for book in books:
            title = book.find('h3').text
            price = book.find(class_="price_color").text

            rating_tag = book.find("p", class_="star-rating")
            rating = rating_tag['class'][1]

            file.write(f"{title}\n")
            file.write(f"{price}\n")
            file.write(f"{rating}\n")
            file.write("\n")

        page_text = doc.find(class_="next")
        if page_text:
            next_href = page_text.find('a')['href']
            if "catalogue/" in next_href:
                url = next_href
            else:
                url = "catalogue/" + next_href
        else:
            url = None
