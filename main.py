from asyncore import write
import csv
import tweepy 
import configparser
import pandas as pd
import json
from datetime import datetime
# from dash import Dash, dash_table

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

most_visited = pd.read_csv('wiki60visited.csv')
most_visited_list = most_visited["City"].values.tolist()
print(most_visited_list)



# read json to Dataframe 
dfcodes = pd.read_json('wcodes.json')
# get list of most visited 
dfcodes = dfcodes[dfcodes['name'].isin(most_visited_list)]
print(dfcodes)
# print(dfcodes)


# # test will small values
# # smalldf = dfcodes.head(4)
# # print(dfcodes)
# # dataframe to list to iterate through
wcodeslist = dfcodes["woeid"].values.tolist()
print(len(wcodeslist))


codes_trends_list = []
# woeid = ''
# loop through codes list 
for wtrends in wcodeslist:
    # print(str(wtrends) + "test")
    trends = api.get_place_trends(id = wtrends)
    for value in trends:
        for trend in value['trends']:
            trend_name = trend['name']
            woeid_codes = wtrends
            # date time value column
            now = datetime.now()
            timestamp_val = now.strftime("%d/%m/%Y %H:%M:%S")
            # print("date and time =", timestamp_val)
            # print(trend_name)
            # print(woeid_codes)
            codes_trends_list.append({'trend_name': trend_name,
                                      'woeid_codes': woeid_codes,
                                      'timestamp': timestamp_val})
        
# print(codes_trends_list)
df_trends_list = pd.DataFrame(codes_trends_list)
print(df_trends_list)

# loop through and replace woeids with city names 
# add_cities = {v['woeid']:v['name'] for v in json_file['wcodes.json'].itervalues()}

# df_trends_list.loc[:, 'woeid'] = df_trends_list['woeid'].map(add_cities)


df_trends_list.to_csv('Trends_File10_21_22.csv')

# datetime object containing current date and time
# now = datetime.now()
 
# # print("now =", now)
# # dd/mm/YY H:M:S
# timestamp_val = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", timestamp_val)



###### plotly code 

    
