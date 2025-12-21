import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random

nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

QUOTES = {
    "positive": [
        "Happiness is not by chance, but by choice.",
        "Your positivity is your superpower.",
        "Keep smiling, life is beautiful."
    ],
    "neutral": [
        "Every moment is a fresh beginning.",
        "Balance is the key to everything.",
        "Pause. Breathe. Continue."
    ],
    "negative": [
        "This too shall pass.",
        "You are stronger than you think.",
        "Bad days do not mean a bad life."
    ]
}

ACTIVITIES = {
    "positive": "Share your happiness with someone or work on a creative task 🎨",
    "neutral": "Go for a short walk or listen to calm music 🎧",
    "negative": "Try deep breathing, journaling, or talking to a friend 🧘"
}

def analyze_sentiment(text):
    scores = sid.polarity_scores(text)
    compound = scores["compound"]

    # Emotion classification
    if compound >= 0.6:
        emotion = "Very Happy 😊"
        mood = "positive"
        color = "success"
        intensity = "High"
    elif compound >= 0.05:
        emotion = "Happy 🙂"
        mood = "positive"
        color = "success"
        intensity = "Medium"
    elif compound > -0.05:
        emotion = "Neutral 😐"
        mood = "neutral"
        color = "warning"
        intensity = "Low"
    elif compound > -0.6:
        emotion = "Sad 😔"
        mood = "negative"
        color = "danger"
        intensity = "Medium"
    else:
        emotion = "Very Sad / Stressed 😢"
        mood = "negative"
        color = "danger"
        intensity = "High"

    # Context-aware suggestions
    text_lower = text.lower()
    if "exam" in text_lower or "study" in text_lower:
        advice = "Academic stress is temporary. Focus on small goals and take breaks 📘"
    elif "job" in text_lower or "career" in text_lower:
        advice = "Career growth takes time. Keep learning and believing in yourself 💼"
    elif "lonely" in text_lower:
        advice = "You’re not alone. Reach out to someone who understands you 💙"
    else:
        advice = ACTIVITIES[mood]

    quote = random.choice(QUOTES[mood])

    return {
        "emotion": emotion,
        "intensity": intensity,
        "quote": quote,
        "advice": advice,
        "scores": scores,
        "color": color,
        "compound": compound
    }
