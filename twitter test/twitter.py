import tweepy
import os


# os.environ.get('CONSUMER_KEY')
# os.environ.get('CONSUMER_SECRET')




# my bearer token is a combo
auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

api = tweepy.API(auth)

# cursor is tweepys way of displaying tweets
# q= is querying "whatever"
# items is the pagination limit of how many are requested
# jerry_twitter =  tweepy.Cursor(api.user_timeline, screen_name="jerryseinfeld").items(5):


def recent_jerry_tweets():
    """Pull last 5 tweets from Jerry."""

    for tweet in tweepy.Cursor(api.user_timeline, screen_name="jerryseinfeld").items(5):
    
        jerry_tweets = tweet.text
        print(jerry_tweets)

def recent_jason_tweets():
    """Pull last 5 tweets from Jerry."""

    for tweet in tweepy.Cursor(api.user_timeline, screen_name="IJasonAlexander").items(5):
    
        jason_tweets = tweet.text
        print(jason_tweets)
