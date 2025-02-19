from transformers import pipeline

emotion_model = pipeline("sentiment-analysis", model="bhadresh-savani/distilbert-base-uncased-emotion")

def detect_emotion(user_text):
    """Detects emotion from user input text."""
    result = emotion_model(user_text)[0]
    return result['label']

if __name__ == "__main__":
    print(detect_emotion("I feel really sad today."))
