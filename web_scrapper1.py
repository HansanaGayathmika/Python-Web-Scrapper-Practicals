from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, 'html.parser')

tag = doc.title
tag.string = "Hello"

tags = doc.find_all("p")[0]
print(tags.find_all("i"))


# with open("changed.html", "w") as file:
#     file.write(str(doc))
