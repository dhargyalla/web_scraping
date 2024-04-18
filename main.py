
import spotipy
from spotipy.oauth2 import SpotifyOAuth
YOUR_CLIENT_ID = '17e7b90042f2417a966cc4042e817bc6'
YOUR_CLIENT_SECRET = 'c66c1108ddbe45a9a920cd0a0d431138'
YOUR_REDIRECT_URI = 'https://example.com/callback/'
SCOPE = 'playlist-modify-private'

# Initialize the SpotifyOAuth object
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(YOUR_CLIENT_ID, YOUR_CLIENT_SECRET, YOUR_REDIRECT_URI)
    )
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

