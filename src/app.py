from fastapi import FastAPI
from sentiment_analysis import detect_emotion
from spotify_api import get_playlist_recommendation

app = FastAPI()

@app.get("/get_playlist/")
def recommend_playlist(text: str):
    """API endpoint to recommend a playlist based on user input."""
    emotion = detect_emotion(text)
    playlist_url = get_playlist_recommendation(emotion)
    return {"emotion": emotion, "playlist": playlist_url}


