from bs4 import BeautifulSoup
import requests

user_choice = input('Enter a year that want to travel back in time (YYYY-MM-DD) : ')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{user_choice}/')
soup = BeautifulSoup(response.text, 'html.parser')

song_names = soup.select('li ul li h3')

for song in song_names:
    print(song.getText().strip())

# Use : https://developer.spotify.com/documentation/web-api/reference/search
# Use : https://gist.github.com/angelabauer/e6087a48f9d1a87d4ec15fc29830892b