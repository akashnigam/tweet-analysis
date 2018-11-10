from tweepy import Cursor
from tweepy import API
import authenticator


class TwitterDataFetcher:

    def __init__(self):
        self.api_instance = API(authenticator.Authenticator().get_auth())

    def get_posted_tweets(self, user, num_tweets):
        user_tweets = []
        for tweet in Cursor(self.api_instance.user_timeline, id=user).items(num_tweets):
            user_tweets.append(tweet)
        return user_tweets


    def get_following_handles(self, user, num):
        user_friends = []
        for friend in Cursor(self.api_instance.friends, id=user).items(num):
            user_friends.append(friend)
        return user_friends


    def get_timeline_tweets(self, user, num_tweets):
        user_timeline_tweets = []
        for tweet in Cursor(self.api_instance.home_timeline, id=user).items(num_tweets):
            user_timeline_tweets.append(tweet)
        return user_timeline_tweets


if __name__ == "__main__":
    user = "msdhoni"
    fetcher = TwitterDataFetcher()
    tweets_posted = fetcher.get_posted_tweets(user,5)
    print(tweets_posted)
    handles_followed = fetcher.get_following_handles(user,5)
    print(handles_followed)
    tweets_in_timeline = fetcher.get_timeline_tweets(user,5)
    print(tweets_in_timeline)