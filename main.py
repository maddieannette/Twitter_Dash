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

most_visited = pd.read_csv('wiki60visited.csv')
most_visited_list = most_visited["City"].values.tolist()
# print(most_visited_list)



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
            # print(trend_name)
            # print(woeid_codes)
            codes_trends_list.append({'trend_name': str(trend_name),
                                      'woeid_codes': str(woeid_codes)})
            #trends_per_country = (str(wtrends) + " " + trend['name'])
            
            # print(trends_per_country)
        # print(type(trend))
        
print(type(codes_trends_list))
# df_trends_list = pd.DataFrame(codes_trends_list, columns = ['trend', 'woeid'])
# print(df_trends_list)
