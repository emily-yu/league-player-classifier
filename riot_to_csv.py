import pandas as pd



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




import requests
import json
## create script to automate riot api sample requests and fill in csv
api_key = input("API KEY: ")




import time
# automate pulling match data from matchURL
# match_urls = [3706043050]
def get_match_data(match_ids):
    result = []
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
        result.append(x)
    return result
        

# pull together different parts of the request
# pull participant username to main stats
def compile_participant_data(request):
    participant_mapping = request["participantIdentities"]
    participant_detail = request["participants"]
    
    # participant_mapping for SELF ONLY
    mapping = next(item for item in participant_mapping if item["player"]["accountId"] == item["player"]["currentAccountId"])
    id = mapping["participantId"]
    p_data = next(item for item in participant_detail if item["participantId"] == id)
    p_data["summonerName"] = mapping["player"]["summonerName"]
    # print(json.dumps(p_data, indent=2)) # full data

    return p_data


# flatten into stats we can use
def flatten(data, participant):
    print(json.dumps(data, indent=2))
    print(json.dumps(participant, indent=2))

    # utility
    def if_true(condition, true, false=None):
        if condition: 
            return true
        return true
    def select_properties(quals, select_from):
        result = {}
        for item in quals: 
            result[item] = select_from[item]
        return result

    stats = participant["stats"]
    props = [
             "summonerName"
             "championId",
             "spell1Id", 
             "spell2Id",
             "item0", 
             "item1", 
             "item2", 
             "item3", 
             "item4", 
             "item5", 
             "item6",
             "perk0",
             "perk0Var1", 
             "perk0Var2",
             "perk0Var3", 
             "perk1",
             "perk1Var1", 
             "perk1Var2",
             "perk1Var3",    
             "perk2",
             "perk2Var1", 
             "perk2Var2",
             "perk2Var3",    
             "perk3",
             "perk3Var1", 
             "perk3Var2",
             "perk3Var3",      
             "perk4",
             "perk4Var1", 
             "perk4Var2",
             "perk4Var3",      
             "perk5",
             "perk5Var1", 
             "perk5Var2",
             "perk5Var3",
             "perkPrimaryStyle",
             "perkSubStyle",
             "statPerk1",
             "statPerk2",
             "role"
             "lane"              
             ]
    qualt_stats = select_properties(props, stats)

    props = [
        "win", # bool
        "kills",
        "deaths",
        "assists",
        "largestKillingSpree",
        "largestMultiKill",
        "killingSprees",
        "longestTimeSpentLiving",
        "doubleKills",
        "tripleKills",
        "quadraKills",
        "pentaKills",
        "unrealKills",
        "totalDamageDealt",
        "magicDamageDealt",
        "physicalDamageDealt",
        "trueDamageDealt",
        "largestCriticalStrike",
        "totalDamageDealtToChampions",
        "magicDamageDealtToChampions",
        "physicalDamageDealtToChampions",
        "trueDamageDealtToChampions",
        "totalHeal",
        "totalUnitsHealed",
        "damageSelfMitigated",
        "damageDealtToObjectives",
        "damageDealtToTurrets",
        "visionScore",
        "timeCCingOthers",
        "totalDamageTaken",
        "magicalDamageTaken",
        "physicalDamageTaken",
        "trueDamageTaken",
        "goldEarned",
        "goldSpent",
        "turretKills",
        "inhibitorKills",
        "totalMinionsKilled",
        "neutralMinionsKilled",
        "neutralMinionsKilledTeamJungle",
        "neutralMinionsKilledEnemyJungle",
        "totalTimeCrowdControlDealt",
        "champLevel",
        "visionWardsBoughtInGame",
        "sightWardsBoughtInGame",
        "wardsPlaced",
        "wardsKilled",
        "firstBloodKill",
        "firstBloodAssist",
        "firstTowerKill",
        "firstTowerAssist",
        "firstInhibitorKill",
        "firstInhibitorAssist",
    ]
    metrics = select_properties(props, stats)
    # convert bools to 1 or 0
    metrics["result"]: if_true(stats["win"] == True, 1, 0)

    return (qualt_stats, metrics)

data = get_match_data(match_urls[0:2])
first_match = data[0].json()

# [TODO]: change compile_participant_data to get all participant data
match_data = compile_participant_data(first_match)
print(json.dumps(match_data, indent=2))

flattened = flatten(first_match, match_data)
def pj(inp):
    print(json.dumps(inp, indent=2))
pj(flattened[0])
pj(flattened[1])