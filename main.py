import tweepy 
import configparser
import pandas as pd
import json

# read config 
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Authentication

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# trends = api.get_place_trends(id = woeid)
api = tweepy.API(auth, wait_on_rate_limit=True)


# read json to Dataframe 
dfcodes = pd.read_json('wcodes.json')
# test will small values
# smalldf = dfcodes.head(4)
# print(dfcodes)
# dataframe to list to iterate through
wcodeslist = dfcodes["woeid"].values.tolist()
# print(wcodeslist)

woeid = ''
# loop through codes list 
for wtrends in wcodeslist:
    # print(str(wtrends) + "test")
    trends = api.get_place_trends(id = wtrends)
    for value in trends:
        for trend in value['trends']:
            print(str(wtrends) + " " + trend['name'])
        # print(type(trend))
        
        # print(trends)
# Get World City Codes
# cityCodes = getCityCodesFromJson(jsonFilePath)
# trendByCity = getTrendsForCityList(cityCodes)
# saveToAwsDatabase(trendByCity)

# def getCityCodesFromJson
#   return json.load(data_file)

# def getTrendsForCityList(cityCodes)
# returnList = {}
# for wdata in cityCodes
#       cityTrends api.get_place_trends(id = woeid)
#       returnList.push(wdata.citycode,cityTrends)

# 
