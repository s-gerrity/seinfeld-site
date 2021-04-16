"""Twitter API connection & queries."""

import tweepy
import os
from model import connect_to_db


consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')


# my bearer token is a combo
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

# "Cursor" is tweepys way of displaying tweets
# q= is querying "whatever"
# ".items" is the pagination limit of how many are requested

tweet_screen_name = {'Jerry': 'jerryseinfeld', 
                    'Julia': 'officialjld', 
                    'Jason': 'IJasonAlexander', 
                    'Modern Seinfeld': 'modern_seinfeld'}


def recent_jerry_tweets(tweet_screen_name):
    """Pull last 5 tweets from Jerry."""

    # create list to collect tweet text
    jerry_tweets = []

    # pull tweet text from API 
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name['Jerry'], include_rts=False).items(5):
        # add the text to the list
        jerry_tweets.append(tweet.text)
       

    return jerry_tweets

def recent_julia_tweets(tweet_screen_name):
    """Pull last 5 tweets from Julia Louis-Dreyfus."""

    julia_tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name['Julia'], include_rts=False).items(5):
        julia_tweets.append(tweet.text)

    return julia_tweets


def recent_jason_tweets(tweet_screen_name):
    """Pull last 5 tweets from Jason Alexander."""

    jason_tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name['Jason'], include_rts=False).items(5):
        jason_tweets.append(tweet.text)

    return jason_tweets

def recent_modern_tweets(tweet_screen_name):
    """Pull last 5 tweets from Modern Seinfeld."""

    modern_tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name['Modern Seinfeld'], include_rts=False).items(5):
        modern_tweets.append(tweet.text)

    return modern_tweets
        

# # # # ##  # DATE CREATED // JERRY ONLY # # # # # ############
def created_at_jerry(tweet_screen_name):
    """Pull dates from last 5 Jerry tweets."""

    jerry_tweet_dates = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name['Jerry']).items(5):
        jerry_tweet_dates.append(tweet.created_at)

    return jerry_tweet_dates


# # # # ##  # LIKES // JERRY ONLY # # # # # ############
def likes_jerry(tweet_screen_name):
    """Pull likes from last 5 Jerry tweets."""

    jerry_likes = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name['Jerry']).items(5):
        jerry_likes.append(tweet.favorite_count)

    return jerry_likes


if __name__ == '__main__':
    from server import app
    connect_to_db(app)