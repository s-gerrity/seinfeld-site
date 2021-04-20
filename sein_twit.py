"""Twitter API connection & functions."""

import tweepy
import os
from model import connect_to_db


consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# "Cursor" is tweepys way of displaying tweets
# q= is querying "whatever"
# ".items" is the pagination limit of how many are requested

tweet_screen_name = {'Jerry': 'jerryseinfeld', 
                    'Julia': 'officialjld', 
                    'Jason': 'IJasonAlexander', 
                    'Modern': 'modern_seinfeld'}


def get_twitter_handle(tweet_screen_name, person):
    """Gets user's Twitter handle, sans re-tweets."""


    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name[person], 
                                                    include_rts=False, 
                                                    tweet_mode='extended',
                                                    ).items(5):
        twitter_handle = tweet.user.screen_name

    return twitter_handle


def get_tweet_id(tweet_screen_name, person):
    """Gets tweet id from last 5 tweets, sans re-tweets."""

    tweet_ids = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name[person], 
                                                    include_rts=False, 
                                                    tweet_mode='extended',
                                                    ).items(5):
        tweet_ids.append(tweet.id)

    return tweet_ids


if __name__ == '__main__':
    from server import app
    connect_to_db(app)