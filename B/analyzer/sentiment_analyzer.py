from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text):
        vader_score = self.analyzer.polarity_scores(text)
        blob_score = TextBlob(text).sentiment.polarity

        print(vader_score, blob_score)
        avg_score = (vader_score['compound'] + blob_score) / 2

        if avg_score >= 0.2:
            return "Позитивная"
        elif avg_score <= -0.2:
            return "Негативная"
        else:
            return "Нейтральная"
