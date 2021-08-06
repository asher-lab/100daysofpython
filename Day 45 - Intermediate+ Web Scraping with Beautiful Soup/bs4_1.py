from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf8") as file:
    contents=file.read()

soup = BeautifulSoup(contents,"html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.h1.string)
print(soup.prettify())
print(soup.p.string)

all_a_tags = (soup.find_all(name="a"))
all_p_tags = (soup.find_all(name="p"))


for tag in all_a_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get("class"))

# Finding only the particular link or anchor tag
# TIP is narrowing it down

company_url = soup.select_one(selector="p a")
print(company_url)

