from bs4 import BeautifulSoup
import requests

url = "https://docs.google.com/forms/d/e/1FAIpQLSdVdrQ9sQAJiBBq0AU-jSYZ45PCitE6F1YxqXmTyEtHVyEOow/viewform"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())

address = soup.find("div", class_="gws-local-maps__address")