import json
import os
# from https://na1.api.riotgames.com/lol/match/v4/matches/3706044908

# load all matches from match folder
matchdata = None
count = 0
for entry in os.scandir('ritoapi_cache/match'):
    with open(entry, 'r') as f2:
        matchdata = f2.read()
        # print(matchdata)
        print(count)
match1 = json.loads(matchdata)
match1 = json.dumps(match1, indent = 2)
# print(match1)
