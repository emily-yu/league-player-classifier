import json

# load singular match from match folder
matchdata = None
with open('ritoapi_cache/match/3706547077.json', 'r') as f2:
    matchdata = f2.read()
    print(matchdata)
match1 = json.loads(matchdata)
match1 = json.dumps(match1, indent = 2)
print(match1)
