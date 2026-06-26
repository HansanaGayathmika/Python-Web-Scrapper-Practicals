from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-windforce-gv-n5080wf3-16gd-geforce-rtx-5080-16gb-graphics-card-triple-fans/p/N82E16814932780?Item=N82E16814932780"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
prices = doc.find_all(string="$")
for price in prices:
    parent = price.parent
    strong = parent.find("strong")

    print(strong.string)
