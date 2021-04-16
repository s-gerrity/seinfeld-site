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


def recent_tweets_text(tweet_screen_name, person):
    """Pull last 5 tweets from Jerry."""

    # create list to collect tweet text
    tweet_list = []

    # pull tweet text from API 
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name[person], include_rts=False).items(5):
        # add the text to the list
        tweet_list.append(tweet.text)
       

    return tweet_list
        

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