import string
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import pandas
import pandas_gbq
import pprint
import neeraj_twitter_credentials

printable = string.printable

if __name__ == '__main__':
    df = pandas.read_csv('../product_list.csv')
    results = []
    for (i, row) in df.iterrows():
        # if i < 137:
        #     continue
        # Authenticate using config.py and connect to Twitter Streaming API.
        hash_tag_list =[ row['name'] ]
        
        fetched_tweets_filename = "tweets.json"

        auth = OAuthHandler(neeraj_twitter_credentials.CONSUMER_KEY, neeraj_twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(neeraj_twitter_credentials.ACCESS_TOKEN, neeraj_twitter_credentials.ACCESS_TOKEN_SECRET)
            
        api = tweepy.API(auth)

        max_tweets = 10
        results = [{
            'Source_Product_Review_ID': 'TWITTER#' + ''.join(str(row['name']).split(' ')) + '#' + str(status.id),
            'Review_Source': "Twitter",
            'Product_Name': row['name'],
            'Product_Category': row['category'],
            'Review_Text': ''.join(filter(lambda x: x in printable, status.text)),
            'User_Id': str(status.user.id),
            'User_Name': status.user.screen_name,
            'Review_date': status.created_at,
            'Location': status.user.location
        } for status in tweepy.Cursor(api.search, q=hash_tag_list).items(max_tweets)]
        print(hash_tag_list[0], results)

        pandas.DataFrame(results).to_csv("twitter.csv", mode='a', header=False)
        # for r in results:

        #     print(r)
        #     project_id = 'dlt-sntmnt-poc-284722'
        #     pandas_gbq.to_gbq(
        #         pandas.DataFrame([r]), 'Sentiment.PRODUCT_REVIEWS_twitter', project_id=project_id, if_exists='append',
            # )
    