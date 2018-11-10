from textblob import TextBlob as tb
import re


class TweetsSentimentAnalyzer:

    @staticmethod
    def clean_tweet(dirty_tweet):
        cleaned_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", dirty_tweet).split())
        return cleaned_tweet

    @staticmethod
    def find_sentiment(tweet):
        analysed_tweet = tb(tweet)
        sentiment = 0
        if analysed_tweet.sentiment.polarity > 0:
            sentiment = 1
        elif analysed_tweet.sentiment.polarity < 0:
            sentiment = -1
        return sentiment

    def clean_and_find_sentiment(self, tweet):
        cleaned_tweet = self.clean_tweet(tweet)
        sentiment = self.find_sentiment(cleaned_tweet)
        return sentiment
