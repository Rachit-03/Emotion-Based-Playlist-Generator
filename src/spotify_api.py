import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))

MOOD_PLAYLISTS = {
    "joy": "happy",
    "anger": "rock",
    "sadness": "sad",
    "fear": "chill",
    "surprise": "energetic",
    "love": "romantic"
}

def get_playlist_recommendation(emotion):
    """Finds a playlist on Spotify based on detected emotion."""
    mood = MOOD_PLAYLISTS.get(emotion.lower(), "chill")
    results = sp.search(q=mood, type='playlist', limit=1)

    if results['playlists']['items']:
        return results['playlists']['items'][0]['external_urls']['spotify']
    return "No playlist found."

if __name__ == "__main__":
    emotion = "joy"
    print(f"Playlist for {emotion}: {get_playlist_recommendation(emotion)}")
