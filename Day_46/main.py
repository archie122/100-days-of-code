from bs4 import BeautifulSoup
import requests

user_choice = input('Enter a year that want to travel back in time (YYYY-MM-DD) : ')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{user_choice}/')
soup = BeautifulSoup(response.text, 'html.parser')

song_names = soup.select('li ul li h3')

for song in song_names:
    print(song.getText().strip())