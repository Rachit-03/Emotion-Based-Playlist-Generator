import streamlit as st
from sentiment_analysis import detect_emotion
from spotify_api import get_playlist_recommendation
import base64

def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

image_path = "E:\\Study\\Project\\EBPG\\background.jpg" 

encoded_image = get_base64_of_image(image_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: Black;
    }}
    .stTextArea>div>div>textarea {{
        background-color: rgba(255, 255, 255, 0.8);
        color: black;
        border-radius: 10px;
        padding: 10px;
    }}
    .stButton>button {{
        background-color: #1DB954;
        color: black;
        border-radius: 20px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        cursor: pointer;
    }}
    .stButton>button:hover {{
        background-color: #1ED760;
    }}
    .stMarkdown {{
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

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
