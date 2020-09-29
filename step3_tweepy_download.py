import string
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import pandas
import pandas_gbq
import pprint
import neeraj_twitter_credentials
import json
from random import randint

printable = string.printable

if __name__ == '__main__':
    df = pandas.read_csv('product_list.csv')
    results = []
    

    fetched_tweets_filename = "tweets.json"
    with open(fetched_tweets_filename, 'a') as tf:
        for (i, row) in df.iterrows():
            if i < 98:
                continue
            # Authenticate using config.py and connect to Twitter Streaming API.
            hash_tag_list =[ row['name'] ]
            

            auth = OAuthHandler(neeraj_twitter_credentials.CONSUMER_KEY, neeraj_twitter_credentials.CONSUMER_SECRET)
            auth.set_access_token(neeraj_twitter_credentials.ACCESS_TOKEN, neeraj_twitter_credentials.ACCESS_TOKEN_SECRET)
                
            api = tweepy.API(auth) #, parser=tweepy.parsers.JSONParser())

            max_tweets = 10
            results = [s for s in tweepy.Cursor(api.search, q=hash_tag_list).items(max_tweets)]
            print(hash_tag_list[0], results)
            for data in results:
                t = {
                    'Source_Product_Review_ID': 'twitter#'+data.user.name+'#'+str(randint(1,500)),
                    'Review_Source': 'Twitter',
                    'Product_Name': row['name'],
                    'Product_Category': row['category'],
                    'Product_Price': None,
                    'Review_Date': data.created_at.isoformat(),
                    'Review_Headline': None,
                    'Review_Text': data.text,
                    'User_ID': data.user.id,
                    'User_Name': data.user.name,
                    'User_Age': None,
                    'User_Location': data.user.location,
                    'Positive_Words': None,
                    'Negetive_Words': None,
                    'Review_Sentiment': None,
                    'Review_Rating': None
                }
                tf.write('\n' + json.dumps(t))

            pandas.DataFrame(results).to_csv("twitter.csv", mode='a', header=False)
        # for r in results:

        #     print(r)
        #     project_id = 'dlt-sntmnt-poc-284722'
        #     pandas_gbq.to_gbq(
        #         pandas.DataFrame([r]), 'Sentiment.PRODUCT_REVIEWS_twitter', project_id=project_id, if_exists='append',
            # )
    