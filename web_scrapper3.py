from bs4 import BeautifulSoup
import re

with open("index2.html", "r")as f:
    doc = BeautifulSoup(f.read(), 'html.parser')

# tag = doc.find("option")
# tag['value'] = "new value"
# tag['selected'] = 'false'
# tag['color'] = 'blue'


# tag = doc.find_all(["p", "div", "li"])

# tag = doc.find_all(['option'], text="Undergraduate", value="undergraduate")

# tag = doc.find_all(class_="btn-item")

# tags = doc.find_all(text=re.compile("\$.*"), limit=2)
# for tag in tags:
#     print(tag.strip())

tags = doc.find_all('input', type='text')
for tag in tags:
    tag['placeholder'] = "i changed you"
print(tags)

with open("changed3.html", "w")as file:
    file.write(str(doc))

# with open("changed1.html", "w") as file:
#     file.write(str(doc))
