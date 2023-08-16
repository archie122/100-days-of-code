import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")
movie_list = [movie_title.getText() for movie_title in movie_titles]
movie_list = movie_list[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
