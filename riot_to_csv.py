import pandas as pd
import requests
import json

df = pd.read_csv('data/challenger_match_V2.csv')
games = df['gameId'].unique()
ind = 0

PLAYER_LIMIT = 50
players_to_follow = []
region = 'kr'

api_key = input("API KEY: ")

while (len(players_to_follow) < PLAYER_LIMIT):
    request_url = 'https://' + region + '.api.riotgames.com/lol/match/v4/matches/' + str(games[ind]) + '?api_key=' + api_key
    x = requests.get(request_url)
    if x.status_code == 200:
        x = x.json()
        for obj in x["participantIdentities"]:
            summonerName = obj["player"]["summonerName"]
            players_to_follow.append(summonerName)
    else:
        # return None
        pass

print(players_to_follow)
print(len(players_to_follow))