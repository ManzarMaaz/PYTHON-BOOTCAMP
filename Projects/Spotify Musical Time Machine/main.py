from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


year = input('Which Year you wanna travel to? (Format= YYYY) :')
month = input(f'Which Month of the Year {year}, (Format= MM) :')
day = input(f'Which Day of the Month {month} and Year {year}, (Format= DD) :')

date_reqd = f"{year}-{month}-{day}"

print(f"\n🎵🎶 Getting Songs from UK's Official Top 100 singles chart on Date {date_reqd}....\n")

header = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0.1 Safari/605.1.15"}

url = "https://www.officialcharts.com/charts/singles-chart/" + date_reqd + "/7501/"

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')

all_titles = soup.find_all("div", class_='description block')

all_songs = []
song_uris = []

for title in all_titles:
    name = title.find("a").getText()

    if "New" in name:
        name = name.replace('New','',1)            

    all_songs.append(name)
    

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="themmm"))

user_id = sp.current_user()["id"]

for song in all_songs:
    result = sp.search(q=f'track:{song} year:{year}', type="track", limit=1)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
        print(f'✅Song name: {song}, Song uri: {uri}')

    except:
        print(f'❌Song Not Found: {song}')
    

playist_name = f"{date_reqd} UK's Official Top 100 singles chart"

print(f'Creating Playlist : {playist_name}')

new_playlist = sp.user_playlist_create(user=user_id,
                                       name=playist_name,
                                       public=False,
                                       description=f"Playlist of UK's Official Top 100 singles chart on Date {date_reqd}")

playlist_id = new_playlist['id']

print(f'Adding {len(song_uris)} Songs to {playist_name} Playlist....')

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

print(f'✅ {len(song_uris)} Songs Successfully added to the Playlist !!!')
