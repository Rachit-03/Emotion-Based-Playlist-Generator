import streamlit as st
from sentiment_analysis import detect_emotion
from spotify_api import get_playlist_recommendation

st.title("🎵 Emotion-Based Playlist Generator")

user_text = st.text_area("How are you feeling today?", "")

if st.button("Get Playlist 🎶"):
    if user_text.strip():
        emotion = detect_emotion(user_text)
        playlist_url = get_playlist_recommendation(emotion)

        st.write(f"**Detected Emotion:** {emotion.capitalize()}")
        st.write(f"🎧 **Recommended Playlist:** [Listen Here]({playlist_url})")
    else:
        st.warning("Please enter some text to analyze your mood.")
