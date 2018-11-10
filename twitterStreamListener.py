from tweepy.streaming import StreamListener
import authenticator
from tweepy import Stream


class TwitterStreamListener(StreamListener):

    def on_data(self, raw_data):
        print(raw_data)

    def on_error(self, status_code):
        print(status_code)


if __name__ == "__main__":
    topic = "life"
    my_listener_obj = TwitterStreamListener()
    auth = authenticator.Authenticator().get_auth()
    actual_stream = Stream(auth, my_listener_obj)
    actual_stream.filter(track=[topic])
