from bs4 import BeautifulSoup
import lxml

with open("website.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a)

all_tags = soup.find_all(name='a')
# print(all_tags)

# for tag in all_tags:
#     # print(tag.getText())
#     print(tag.get('href'))

heading = soup.find(name='h1', id='name')
# print(heading.getText())

section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.getText())

company_url = soup.select_one('p a')
# print(company_url.get('href'))

name = soup.select_one(selector="#name")
# print(name)

heading = soup.select(".heading")
print(heading)