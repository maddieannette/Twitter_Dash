import tweepy 
import configparser

#read config 
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

print(api_key)

# auth = tweepy.OAuth1UserHandler(
#     consumer_key, consumer_secret, access_token, access_token_secret
# )

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)