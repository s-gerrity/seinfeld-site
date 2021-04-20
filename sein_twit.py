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
                    'Modern Seinfeld': 'modern_seinfeld'}


def recent_tweets_text(tweet_screen_name, person):
    """Pull last 5 tweets from user, sans re-tweets."""

    tweet_list = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name[person], 
                                                  include_rts=False, 
                                                  tweet_mode='extended'
                                                  ).items(5):
        tweet_list.append(tweet.full_text)
       

    return tweet_list
        

def created_at_date(tweet_screen_name, person):
    """Pull dates from last 5 tweets, sans re-tweets."""

    created_at_dates = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name[person], 
                                                  include_rts=False
                                                  ).items(5):
        created_at_dates.append(tweet.created_at)

    return created_at_dates


def tweet_likes(tweet_screen_name, person):
    """Pull likes(favorite count) from last 5 user tweets, sans re-tweets."""

    tweet_likes = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name[person], 
                                                  include_rts=False
                                                  ).items(5):
        tweet_likes.append(tweet.favorite_count)

    return tweet_likes


def get_profile_image(tweet_screen_name, person):
    """Get each Twitter accounts profile image."""

    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name[person]).items(1):
        twitter_profile_image = tweet.user.profile_image_url

        return twitter_profile_image

    
def recent_tweets_url(tweet_screen_name, person):
    """Pull last 5 tweets from user, sans re-tweets."""

    
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name[person], 
                                                  include_rts=False, 
                                                  tweet_mode='extended',
                                                  ).items(5):
        twitter_image = tweet.user.url

    return twitter_image


def tweets_expanded_url(tweet_screen_name, person):
    """Pull last 5 tweets from user, sans re-tweets."""

    
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name[person], 
                                                  include_rts=False, 
                                                  tweet_mode='extended',
                                                  ).items(5):
        twitter_user_name = tweet.user.name
        twitter_id = tweet.id

        twitter_expanded_url = f"https://twitter.com/{twitter_user_name}/status/{twitter_id}"
       

    return twitter_expanded_url


def get_twitter_username(tweet_screen_name, person):
    """Pull last 5 tweets from user, sans re-tweets."""


    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name[person], 
                                                    include_rts=False, 
                                                    tweet_mode='extended',
                                                    ).items(5):
        twitter_username = tweet.user.name

    return twitter_username


def get_twitter_handle(tweet_screen_name, person):
    """Pull last 5 tweets from user, sans re-tweets."""


    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tweet_screen_name[person], 
                                                    include_rts=False, 
                                                    tweet_mode='extended',
                                                    ).items(5):
        twitter_handle = tweet.user.screen_name

    return twitter_handle


if __name__ == '__main__':
    from server import app
    connect_to_db(app)