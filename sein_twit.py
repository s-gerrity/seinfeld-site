import tweepy
import os
from model import connect_to_db


# os.environ.get('CONSUMER_KEY')
# os.environ.get('CONSUMER_SECRET')


# my bearer token is a combo
auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

api = tweepy.API(auth)

# cursor is tweepys way of displaying tweets
# q= is querying "whatever"
# items is the pagination limit of how many are requested
# jerry_twitter =  tweepy.Cursor(api.user_timeline, screen_name="jerryseinfeld").items(5):

tweet_screen_name = {'Jerry': 'jerryseinfeld', 'Julia': 'officialjld', 'Jason': 'IJasonAlexander', 'Modern Seinfeld': 'modern_seinfeld'}


def recent_jerry_tweets(tweet_screen_name):
    """Pull last 5 tweets from Jerry."""

    jerry_tweets = []
        
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name['Jerry']).items(5):

        jerry_tweets.append(tweet.text)

    return jerry_tweets

def recent_julia_tweets(tweet_screen_name):
    """Pull last 5 tweets from Julia Louis-Dreyfus."""

    julia_tweets = []
        
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name['Julia']).items(5):

        julia_tweets.append(tweet.text)

    return julia_tweets


def recent_jason_tweets(tweet_screen_name):
    """Pull last 5 tweets from Jason Alexander."""

    jason_tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name['Jason']).items(5):
        
        jason_tweets.append(tweet.text)

    return jason_tweets

def recent_modern_tweets(tweet_screen_name):
    """Pull last 5 tweets from Modern Seinfeld."""

    modern_tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name['Modern Seinfeld']).items(5):
        
        modern_tweets.append(tweet.text)

    return modern_tweets
        
if __name__ == '__main__':
    from server import app
    connect_to_db(app)