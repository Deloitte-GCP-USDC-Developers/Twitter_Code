from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import pprint
import neeraj_twitter_credentials

# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """    Class for streaming and processing live tweets."""
    def __init__(self):
        pass
    
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(neeraj_twitter_credentials.CONSUMER_KEY, neeraj_twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(neeraj_twitter_credentials.ACCESS_TOKEN, neeraj_twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """    This is a basic listener that just prints received tweets to stdout."""
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True


    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list =[ "Sony Playstation VR" ]
    
    fetched_tweets_filename = "tweets.json"

    auth = OAuthHandler(neeraj_twitter_credentials.CONSUMER_KEY, neeraj_twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(neeraj_twitter_credentials.ACCESS_TOKEN, neeraj_twitter_credentials.ACCESS_TOKEN_SECRET)
        
    api = tweepy.API(auth)

    max_tweets = 100
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=hash_tag_list).items(max_tweets)]
    print([t.entities['urls'][0]['url'] for t in searched_tweets if len(t.entities['urls']) > 0])