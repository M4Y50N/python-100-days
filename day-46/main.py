import time

from bs4 import BeautifulSoup
import requests
import lxml

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
import os

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

# date_input = input("Which year you want to travel to? Type the date in this format YYYY-MM-DD:")
# year = date_input.split("-")[0]
# response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_input}/")
#
# soup = BeautifulSoup(response.text, "lxml")
#
# get_songs = soup.select(".o-chart-results-list__item #title-of-a-story")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://music.youtube.com/watch?v=1i0i5lG6Ojc&si=rF5gX5MzEDdnNOGX")

time.sleep(5)
get_songs = driver.find_elements(By.CSS_SELECTOR, value="#automix-contents .song-title")

songs = []
for song in get_songs:
    songs.append(song.text.split("(")[0].split("[")[0])

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

client_credentials = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI,
                                  scope="playlist-modify-private")
spotify = spotipy.Spotify(client_credentials_manager=client_credentials)

user_id = spotify.current_user()["id"]

# Get songs url
songs_url = []
for song in songs:
    result = spotify.search(q=f"track:{song}", type="track")
    try:
        songs_url.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"'{song}' doesn't exist in Spotify. Skipped.")

playlist = spotify.user_playlist_create(user=user_id, name=f"Saahirah Liked Songs Playlist", public=False)
# print(playlist["id"])

spotify.playlist_add_items(playlist["id"], songs_url)

# CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
# CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
# REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
#
# client_credentials = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI,
#                                   scope="playlist-modify-private")
# spotify = spotipy.Spotify(client_credentials_manager=client_credentials)
#
# user_id = spotify.current_user()["id"]
#
# # Get songs url
# songs_url = []
# for song in songs:
#     result = spotify.search(q=f"track:{song} year:{year}", type="track")
#     try:
#         songs_url.append(result["tracks"]["items"][0]["uri"])
#     except IndexError:
#         print(f"'{song}' doesn't exist in Spotify. Skipped.")
#
# playlist = spotify.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)
# # print(playlist["id"])
#
# spotify.playlist_add_items(playlist["id"], songs_url)

