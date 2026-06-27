from bs4 import BeautifulSoup
import requests

base_url = "http://quotes.toscrape.com/"
url = "/"

with open(r"C:\\Users\\Hansana\\Desktop\\web_scrapper\\quotes.csv", "w", encoding="utf-8")as file:
    while url:
        page = requests.get(base_url + url).text
        doc = BeautifulSoup(page, "html.parser")

        quotes = doc.find_all(class_="quote")

        for quote in quotes:
            text = quote.find('span').text
            author = quote.find(class_="author").text
            file.write(f"{text}\n")
            file.write(f"{author}\n")
            tags = quote.find_all("a", class_="tag")
            for tag in tags:
                file.write(f"{tag.text}\n")

            file.write("\n")

        page_text = doc.find(class_="next")
        if page_text:
            url = page_text.find('a')['href']
        else:
            url = None
