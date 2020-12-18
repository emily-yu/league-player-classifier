#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("challenjourrrrr")


# In[2]:


# setup
get_ipython().system('pip install xlrd')
import pandas as pd


# In[3]:


# read in initial csv 

df = pd.read_csv('data/challenger_match_V2.csv')
players = df['accountId'].unique()

playerLimit = 5 # temporary - for testing
for player in players:

    # for testing
    playerLimit -= 1
    if playerLimit == 0: break

    player_games = df[df['accountId'] == player]
    player_games = player_games.drop(columns=['accountId'])
    print(player)
    print(player_games['gameId'].to_list())

    match_urls = player_games['gameId'].to_list() #for testing bottom function


# In[4]:


import requests
import json
## create script to automate riot api sample requests and fill in csv
api_key = input("API KEY: ")


# In[5]:


# automate pull matches from summonerids


# In[ ]:





# In[6]:


import time
# automate pulling match data from matchURL
# match_urls = [3706043050]
def get_match_data(match_ids):
    for match_id in match_ids:
        request_url = 'https://kr.api.riotgames.com/lol/match/v4/matches/' + str(match_id) + '?api_key=' + api_key
        print(request_url)
        x = requests.get(request_url)
        # if x.status_code == 429: # to go rapidfire...
        #     print("429", ind)
        #     sleep(125) # sleep for 2 minutes + 5 seconds in case
        #     x = requests.get(request_url) # retry

        # but lets be a good boy and only make one request every second
        time.sleep(1)

        print(json.dumps(x.json(), indent=2))
        
get_match_data(match_urls[0:5])
# print(match_urls)


# In[7]:


# perform similar clustering to 

