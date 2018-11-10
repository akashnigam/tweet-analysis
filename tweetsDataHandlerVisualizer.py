import pandas as pd
import numpy as np
import matplotlib.pyplot as mlpp
import twitterDataFetcher


class TweetsDataHandlerVisualizer:

    def __init__(self, user, num_tweets):
        self.fetcher = twitterDataFetcher.TwitterDataFetcher()
        self.data_frame = self.get_user_tweets_dataframe(user, num_tweets)

    def get_user_tweets_dataframe(self, user, num_tweets):
        tweets = self.fetcher.get_posted_tweets(user, num_tweets)
        data_frame = pd.DataFrame()
        data_frame["text"] = np.array([tweet.text for tweet in tweets])
        data_frame["ids"] = np.array([tweet.id for tweet in tweets])
        data_frame["len"] = np.array([len(tweet.text) for tweet in tweets])
        data_frame["date"] = np.array([tweet.created_at for tweet in tweets])
        data_frame["source"] = np.array([tweet.source for tweet in tweets])
        data_frame["like"] = np.array([tweet.favorite_count for tweet in tweets])
        data_frame["retweets"] = np.array([tweet.retweet_count for tweet in tweets])
        return data_frame

    @staticmethod
    def normalize_data_frame_column(column_data):
        norm = np.linalg.norm(column_data, ord=1)
        normalized_column_data = column_data/norm
        return normalized_column_data

    def map_user_tweets_likes_by_date(self):
        time_likes = pd.Series(self.data_frame["like"].values, self.data_frame["date"].values)
        time_likes.plot(figsize=(16, 4), color="g")
        mlpp.show()

    def map_user_tweets_length_by_date(self):
        time_length = pd.Series(self.data_frame["len"].values, self.data_frame["date"].values)
        time_length.plot(figsize=(16, 4), color="g")
        mlpp.show()

    def map_user_tweets_retweets_by_date(self):
        time_retweets = pd.Series(self.data_frame["retweets"].values, self.data_frame["date"].values)
        time_retweets.plot(figsize=(16, 4), color="b")
        mlpp.show()

    def map_user_tweets_length_likes_retweets__by_date(self):
        norm_lengths = self.normalize_data_frame_column(self.data_frame["len"].values)
        time_length = pd.Series(norm_lengths, self.data_frame["date"].values)
        time_length.plot(figsize=(16, 4), label="length", legend="true")
        norm_likes = self.normalize_data_frame_column(self.data_frame["like"].values)
        time_likes = pd.Series(norm_likes, self.data_frame["date"].values)
        time_likes.plot(figsize=(16, 4), label="likes", legend="true")
        norm_retweets = self.normalize_data_frame_column(self.data_frame["retweets"].values)
        time_retweets = pd.Series(norm_retweets, self.data_frame["date"].values)
        time_retweets.plot(figsize=(16, 4), label="retweets", legend="true")
        mlpp.show()


if __name__ == "__main__":
    user = "msdhoni"
    num_of_tweets = 100
    visualizer = TweetsDataHandlerVisualizer(user, num_of_tweets)
    visualizer.map_user_tweets_length_by_date()
    visualizer.map_user_tweets_likes_by_date()
    visualizer.map_user_tweets_retweets_by_date()
    visualizer.map_user_tweets_length_likes_retweets__by_date()
