from transformers import pipeline
from textblob import TextBlob
import re

# Sentiment and tone detection using HuggingFace or TextBlob
sentiment_analyzer = pipeline("sentiment-analysis")
emotion_keywords = ["confident", "nervous", "happy", "angry", "sad", "neutral"]

def analyze_text(text):
    """
    Analyze text for sentiment, tone, clarity, and confidence.
    """
    # Sentiment
    sentiment_result = sentiment_analyzer(text)
    
    # Clarity / filler word analysis
    filler_words = ["um", "uh", "like", "you know"]
    filler_count = sum([text.lower().count(w) for w in filler_words])
    
    # Confidence estimation (simple heuristic)
    confidence_score = max(0, 100 - filler_count * 5)
    
    # Emotional keywords detection
    detected_emotions = [word for word in emotion_keywords if re.search(rf"\b{word}\b", text.lower())]
    
    # Grammar / coherence (TextBlob for simplicity)
    blob = TextBlob(text)
    grammar_errors = len(blob.correct())  # Simplified
    
    analysis = {
        "sentiment": sentiment_result[0]['label'],
        "sentiment_score": sentiment_result[0]['score'],
        "filler_words_count": filler_count,
        "confidence_score": confidence_score,
        "detected_emotions": detected_emotions,
        "grammar_check": grammar_errors
    }
    
    return analysis
