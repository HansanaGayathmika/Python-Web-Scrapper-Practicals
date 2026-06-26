from bs4 import BeautifulSoup
import re
import requests

search_item = input("What product do yuo want to search for? ")

url = f"https://www.newegg.com/p/pl?d={search_item}&N=4131"

page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:1])
print(pages)

items_found = {}

for page in range(1, pages + 1):
    url = f"https://www.newegg.com/p/pl?d={search_item}&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(
        class_="item-cells-wrap border-cells short-video-box items-list-view is-list")

    items = div.find_all(text=re.compile(search_item))

    for item in items:
        parent = item.parent

        if parent.name != "a":
            continue

        link = parent['href']

        next_parent = parent.parent
        price = div.find(class_="price-current").strong.string

        items_found[item] = {"price": int(
            price.replace(",", "")), "link": link}

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

with open(r"C:\Users\Hansana\Desktop\web_scrapper\gpu3080.csv", "w")as file:

    for item in sorted_items:

        name = item[0]
        price = item[1]['price']
        link = item[1]['link']

        file.write(f"{name}\n")
        file.write(f"{price}\n")
        file.write(f"{link}\n")
        file.write("\n")

        # print(item[0])
        # print(f"${item[1]['price']}")
        # print(item[1]['link'])
        # print()


# for item, data in items_found:
#     print("Item: ", item)
#     print("Price: ", data["price"])
#     print("Link: ", data["link"])
