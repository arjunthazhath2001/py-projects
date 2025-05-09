import requests
from bs4 import BeautifulSoup
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID_SPOTIFY = os.getenv('CLIENT_ID_SPOTIFY')

CLIENT_SECRET_SPOTIFY = os.getenv('CLIENT_SECRET_SPOTIFY')

URL_REDIRECT = "https://example.com"

# Step 1: Authenticate and get token
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID_SPOTIFY, 
                        client_secret=CLIENT_SECRET_SPOTIFY, 
                        redirect_uri=URL_REDIRECT,
                        scope="playlist-modify-private")

token_info = sp_oauth.get_access_token(as_dict=False)
access_token = token_info

# Step 2: Use token to create Spotify object
sp = Spotify(auth=access_token)

# Step 3: Now you can call API methods
username = sp.current_user()["id"]


headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

userdate= input("which date u want? ENter as YYYY-MM-DD") 
year = userdate.split("-")[0]

response= requests.get(url=f"https://www.billboard.com/charts/hot-100/{userdate}", headers=headers)

billboard=response.text

soup= BeautifulSoup(billboard,"html.parser")

song_titles= soup.select("li ul li h3")
song_names= [song.getText().strip() for song in song_titles]

song_uris=[]
for song in song_names:
    result= sp.search(q=f"track:{song} year:{year}", type="track")
   
    try:
        uri= result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist")


created= sp.user_playlist_create(username, name=f"{userdate} Billboard 100", public=False, collaborative=False, description='')
playlist_id= created["id"]
print(playlist_id)


inserted= sp.user_playlist_add_tracks(username, playlist_id, tracks=song_uris, position=None)

print(inserted)