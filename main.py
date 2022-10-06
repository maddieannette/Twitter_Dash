import tweepy 
import configparser
import pandas as pd

#read config 
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# test
# print(api_key)

# Authentication

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_id = 'NHSuk'
count = 20
trim_user = True

statuses = api.get_user(user_id)

print(statuses)
# print(public_tweets)
# print(public_tweets[0].text)

# to pull all tweets 
# for tweet in public_tweets:
#     print(tweet.text)


