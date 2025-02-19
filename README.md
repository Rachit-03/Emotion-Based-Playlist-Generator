Emotion-Based Playlist Generator

📌 Project Overview

The **Emotion-Based Playlist Generator** is a Python application that analyzes user input to detect emotions and suggests Spotify playlists accordingly. It uses **NLP-based sentiment analysis** to understand user moods and integrates with the **Spotify API** to fetch playlists that match the detected emotion.

🚀 Features

- 🔍 **Sentiment Analysis** – Uses Hugging Face Transformers to classify emotions.
- 🎧 **Spotify API Integration** – Fetches curated playlists based on user mood.
- 🌐 **Web Interface** – Built with **Streamlit** for an easy-to-use UI.
- 🔥 **FastAPI Backend** – Provides an API for retrieving playlists programmatically.
- 📊 **Scalable & Lightweight** – Uses pre-trained models and APIs for efficiency.

🛠 Tech Stack

- **Programming Language:** Python
- **Libraries:** Transformers, spaCy, NLTK, Spotipy, LangChain
- **Frameworks:** Streamlit (UI), FastAPI (Backend)
- **APIs:** Spotify Web API, OpenAI API (optional for better sentiment interpretation)

📂 Project Structure

```
📁 Emotion-Based-Playlist-Generator
│── 📁 src
│   │── sentiment_analysis.py   # Sentiment detection logic
│   │── spotify_api.py          # Spotify API integration
│   │── app.py                  # FastAPI backend
│   │── ui.py                   # Streamlit UI
│── .env                        # Store Spotify API keys (optional)
│── requirements.txt            # Dependencies
│── README.md                   # Project Documentation
```

🔧 Setup & Installation 

 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Emotion-Based-Playlist-Generator.git
cd Emotion-Based-Playlist-Generator
```

 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

 3️⃣ Set Up Spotify API

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create an app & get **Client ID** and **Client Secret**
3. Create a `.env` file in the root directory and add:
   ```
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   ```

🚀 Running the Project

 1️⃣ Start the FastAPI Backend

```bash
uvicorn app:app --reload
```

 2️⃣ Run the Streamlit UI

```bash
streamlit run ui.py
```

🎯 Usage

- Open the Streamlit UI.
- Enter a text description of your mood (e.g., *"I feel happy today!"*).
- The app detects the sentiment and provides a **Spotify playlist recommendation**.
- Click on the playlist link to listen directly on Spotify.
