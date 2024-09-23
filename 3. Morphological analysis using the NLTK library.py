
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def sentiment_analysis(text):
    
    scores = sia.polarity_scores(text)
    if scores['compound'] > 0.05:
        sentiment = "Positive"
    elif scores['compound'] < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return scores, sentiment
text = "I love this product! It's amazing."
scores, sentiment = sentiment_analysis(text)
print("Sentiment Scores:")
print(f"  - Positive: {scores['pos']:.2f}")
print(f"  - Negative: {scores['neg']:.2f}")
print(f"  - Neutral: {scores['neu']:.2f}")
print(f"  - Compound: {scores['compound']:.2f}")
print(f"\nSentiment: {sentiment}")
