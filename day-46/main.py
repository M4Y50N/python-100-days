from bs4 import BeautifulSoup
import requests
import lxml

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
import os

load_dotenv()

# data_input = input("Which year you want to travel to? Type the date in this format YYYY-MM-DD:")
data_input = "2023-03-04"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{data_input}/")

soup = BeautifulSoup(response.text, "lxml")

get_songs = soup.select(".o-chart-results-list__item #title-of-a-story")
songs = []
for song in get_songs:
    songs.append(song.get_text().strip())

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

client_credentials = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials)

print(spotify.current_user()["id"])
