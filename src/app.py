import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secreta = os.environ.get("CLIENT_SECRET")



auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secreta)
spotify = spotipy.Spotify(auth_manager=auth_manager)


artist_id = "0W4t58pS2IXD4R8CTj2zH7"

results = spotify.artist_top_tracks(artist_id)

canciones = []
for track in results['tracks']:
    canciones.append({
        'nombre': track['name'],
        'popularidad': track['popularity'],
        'duracion': track['duration_ms'] / 60000
    })


df = pd.DataFrame(canciones)