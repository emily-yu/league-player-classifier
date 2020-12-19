import pandas as pd



# df = pd.read_csv('data/.csv')
df = pd.read_excel('league_pro_matches_data/2019-spring-match-data-OraclesElixir-2019-05-21.xlsx')
match_urls = df['gameid'].unique()
print(match_urls)


# playerLimit = 10 # temporary - for testing
# match_urls = []
# for player in players:

#     # # for testing
#     # playerLimit -= 1
#     # if playerLimit == 0: break

#     player_games = df[df['accountId'] == player]
#     player_games = player_games.drop(columns=['accountId'])
#     print(player)
#     print(player_games['gameId'].to_list())

#     match_urls += player_games['gameId'].to_list() #for testing bottom function




# import requests
# import json
# ## create script to automate riot api sample requests and fill in csv
# api_key = input("API KEY: ")




# import time
# # automate pulling match data from matchURL
# # match_urls = [3706043050]
# def get_match_data(match_ids):
#     result = []
#     for match_id in match_ids:
#         request_url = 'https://kr.api.riotgames.com/lol/match/v4/matches/' + str(match_id) + '?api_key=' + api_key
#         print(request_url)
#         x = requests.get(request_url)
#         print(x.status_code)
#         while x.status_code == 429: # to go rapidfire...
#             # print("429", ind)
#             # time.sleep(125) # sleep for 2 minutes + 5 seconds in case
#             # time.sleep(60) # sleep for 1 min bc my computer is slow lul
#             print("headers:", x.headers)
#             time.sleep(float(x.headers['Retry-After']))
#             x = requests.get(request_url) # retry

#         # if x.status_code == 504: 
#         #     print("unlucky")
#         if x.status_code == 200:
#             # but lets be a good boy and only make one request every second
#             # time.sleep(1/2)

#             # print(json.dumps(x.json(), indent=2))
#             result.append(x)
#             print(len(result))
#         else:
#             pass

#     return result
        

# # pull together different parts of the request
# # pull participant username to main stats
# def compile_participant_data(request):
#     participant_mapping = request["participantIdentities"]
#     participant_detail = request["participants"]
    
#     # participant_mapping for SELF ONLY
#     mapping = next(item for item in participant_mapping if item["player"]["accountId"] == item["player"]["currentAccountId"])
#     id = mapping["participantId"]
#     p_data = next(item for item in participant_detail if item["participantId"] == id)
#     p_data["summonerName"] = mapping["player"]["summonerName"]
#     # print(json.dumps(p_data, indent=2)) # full data

#     return p_data


# # flatten into stats we can use
# def flatten(data, participant):
#     # print(json.dumps(data, indent=2))
#     # print(json.dumps(participant, indent=2))

#     # utility
#     def if_true(condition, true, false=None):
#         if condition: 
#             return true
#         return true
#     def select_properties(quals, select_from, prefix=''):
#         result = {}
#         for item in quals: 

#             # ensure key is there, if not signal taht isn't there
#             if item not in select_from:
#                 result[prefix+item] = "NaN"
#                 return result

#             # convert bools to 1 or 0
#             if isinstance(select_from[item], bool):
#                 select_from[item] = int(select_from[item] == True)
#             result[prefix+item] = select_from[item]
#         return result

#     stats = participant["stats"]
#     props = [
#              "item0", 
#              "item1", 
#              "item2", 
#              "item3", 
#              "item4", 
#              "item5", 
#              "item6",
#              "perk0",
#              "perk0Var1", 
#              "perk0Var2",
#              "perk0Var3", 
#              "perk1",
#              "perk1Var1", 
#              "perk1Var2",
#              "perk1Var3",    
#              "perk2",
#              "perk2Var1", 
#              "perk2Var2",
#              "perk2Var3",    
#              "perk3",
#              "perk3Var1", 
#              "perk3Var2",
#              "perk3Var3",      
#              "perk4",
#              "perk4Var1", 
#              "perk4Var2",
#              "perk4Var3",      
#              "perk5",
#              "perk5Var1", 
#              "perk5Var2",
#              "perk5Var3",
#              "perkPrimaryStyle",
#              "perkSubStyle",
#              "statPerk1",
#              "statPerk2",            
#              ]
#     qualt_stats = select_properties(props, stats)
#     props = [
#         "summonerName",
#         "championId",
#         "spell1Id", 
#         "spell2Id",
#     ]
#     qualt_stats.update(select_properties(props, participant))
#     props = [
#         "role",
#         "lane"  
#     ]
#     qualt_stats.update(select_properties(props, participant["timeline"]))

#     props = [
#         "win", # bool
#         "kills",
#         "deaths",
#         "assists",
#         "largestKillingSpree",
#         "largestMultiKill",
#         "killingSprees",
#         "longestTimeSpentLiving",
#         "doubleKills",
#         "tripleKills",
#         "quadraKills",
#         "pentaKills",
#         "unrealKills",
#         "totalDamageDealt",
#         "magicDamageDealt",
#         "physicalDamageDealt",
#         "trueDamageDealt",
#         "largestCriticalStrike",
#         "totalDamageDealtToChampions",
#         "magicDamageDealtToChampions",
#         "physicalDamageDealtToChampions",
#         "trueDamageDealtToChampions",
#         "totalHeal",
#         "totalUnitsHealed",
#         "damageSelfMitigated",
#         "damageDealtToObjectives",
#         "damageDealtToTurrets",
#         "visionScore",
#         "timeCCingOthers",
#         "totalDamageTaken",
#         "magicalDamageTaken",
#         "physicalDamageTaken",
#         "trueDamageTaken",
#         "goldEarned",
#         "goldSpent",
#         "turretKills",
#         "inhibitorKills",
#         "totalMinionsKilled",
#         "neutralMinionsKilled",
#         "neutralMinionsKilledTeamJungle",
#         "neutralMinionsKilledEnemyJungle",
#         "totalTimeCrowdControlDealt",
#         "champLevel",
#         "visionWardsBoughtInGame",
#         "sightWardsBoughtInGame",
#         "wardsPlaced",
#         "wardsKilled",
#         "firstBloodKill",
#         "firstBloodAssist",
#         "firstTowerKill",
#         "firstTowerAssist",
#         "firstInhibitorKill",
#         "firstInhibitorAssist",
#     ]
#     metrics = select_properties(props, stats)

#     props = [
#         "0-10",
#         "10-20",
#         "20-30",
#     ]
#     participant_key = ["creepsPerMinDeltas", "xpPerMinDeltas", "goldPerMinDeltas", "xpDiffPerMinDeltas", "damageTakenPerMinsDeltas", "damageTakenDiffPerMinsDeltas"]
#     for key in participant_key: 
#         if key in participant["timeline"]:
#             metrics.update(select_properties(props, participant["timeline"][key], key))
#         else:
#             metrics.update({
#                 key + "0-10": "NaN",
#                 key + "10-20": "NaN",
#                 key + "20-30": "NaN",
#             })
#     # metrics.update(select_properties(props, participant["timeline"]["creepsPerMinDeltas"], 'creepsPerMin'))
#     # metrics.update(select_properties(props, participant["timeline"]["xpPerMinDeltas"], 'xpPerMin'))
#     # metrics.update(select_properties(props, participant["timeline"]["goldPerMinDeltas"], 'goldPerMin'))
#     # metrics.update(select_properties(props, participant["timeline"]["csDiffPerMinDeltas"], 'csDiffPerMin'))
#     # metrics.update(select_properties(props, participant["timeline"]["xpDiffPerMinDeltas"], 'xpDiffPerMin_'))
#     # metrics.update(select_properties(props, participant["timeline"]["damageTakenPerMinDeltas"], 'damageTakenPerMin_'))
#     # metrics.update(select_properties(props, participant["timeline"]["damageTakenDiffPerMinDeltas"], 'damageTakenDiffPerMin_'))

#     return (qualt_stats, metrics)

# # data = get_match_data(match_urls[0:10000])
# data = get_match_data(match_urls[0:10])
# # data = get_match_data(match_urls)

# writeable = []
# writeableq = [] # qualitative values (not used for clustering)
# for first_match in data:
# # first_match = data[0].json()
#     first_match = first_match.json()

#     # [TODO]: change compile_participant_data to get all participant data
#     match_data = compile_participant_data(first_match)
#     # print(json.dumps(match_data, indent=2))

#     flattened = flatten(first_match, match_data)
#     def pj(inp):
#         print(json.dumps(inp, indent=2))
#     # pj(flattened[0])
#     # pj(flattened[1])

#     base = {
#         "summonerName": flattened[0]["summonerName"]
#     } 
#     base.update(flattened[1])
#     # flattened[1]["summonerName"] = flattened[0]["summonerName"] # port over for now otherwise no identification
#     # writeable.append(flattened[1])
#     writeable.append(base)

#     base = {
#         "summonerName": flattened[0]["summonerName"]
#     }
#     base.update(flattened[0])
#     writeableq.append(base)

# # put into csv
# import csv
# def to_csv(row, filepath):
#     with open(filepath, 'a') as f:  # Just use 'w' mode in 3.x
#         w = csv.DictWriter(f, row.keys())
#         w.writerow(row)

# ### write header
# with open('write_quant_pro.csv', 'w') as f:  # Just use 'w' mode in 3.x
#     w = csv.DictWriter(f, writeable[0].keys())
#     w.writeheader()
# with open('write_qual_pro.csv', 'w') as f:  # Just use 'w' mode in 3.x
#     w = csv.DictWriter(f, writeableq[0].keys())
#     w.writeheader()

# ### write data
# for match in writeable:
#     to_csv(match, 'write_quant_pro.csv')




# ### write qualitative data

# # conversions for qualitative data (ids in riot system) to filtering
# def process_champion_data(id):
#     x = requests.get('https://cdn.communitydragon.org/10.25.1/champion/' + str(id) + '/data')
#     return x.json()["name"]

# # championName = process_champion_data(83)
# # print(championName)

# def process_item_data(item_number):
#     f = open('cdragon_en_US/item.json') 
#     items = json.load(f)

#     # catch nonexistent lul
#     if str(item_number) not in items["data"]: 
#         return "NaN"

#     return items["data"][str(item_number)]["name"]

# # itemName = process_item_data(3153)
# # print(itemName)

# def process_perk_data(perkData): # [perk1, perk1Var1, perk1Var2, perk1Var3]
#     # edge case
#     if perkData == 0:
#         return ""

#     f = open('cdragon_en_US/runesReforged.json') 
#     runes = json.load(f)
#     # flatten
#     flattened = []
#     # print("flatten")
#     # print(json.dumps(runes, indent=2))
#     for i in range(len(runes)):
#         for elem in runes[i]["slots"]: 
#             flattened += elem["runes"]

#     # print(json.dumps(flattened, indent=2))
#     result = next((x for x in flattened if x["id"] == perkData), None)

#     # catch nonexistent lul
#     if result is None:
#         return 'NaN'

#     return result["key"]

# # perkName = process_perk_data(8237)
# # print(perkName)

# def process_spell_data(spell_id):
#     f = open('cdragon_en_US/summoner.json') 
#     summoner_metadata = json.load(f)
#     # flatten
#     flattened = []
#     # print("flatten")
#     # print(json.dumps(summoner_metadata["data"], indent=2))
#     result = next((summoner_metadata["data"][i] for i in summoner_metadata["data"] if summoner_metadata["data"][i]["key"] == str(spell_id)), None)
#     # print('result', result)

#     if result is None:
#         return 'NaN'
    
#     return result["name"]

# # spellName = process_spell_data(12)
# # print(spellName)

# # replace item names
# for match in writeableq:
#     props = ['item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6']
#     for key in range(len(props)):
#         item_id = props[key]
#         match[item_id] = process_item_data(match[item_id])
    
#     props = [
#         'perk0', 'perk0Var1', 'perk0Var2', 'perk0Var3', 
#         'perk1', 'perk1Var1', 'perk1Var2', 'perk1Var3', 
#         'perk2', 'perk2Var1', 'perk2Var2', 'perk2Var3', 
#         'perk3', 'perk3Var1', 'perk3Var2', 'perk3Var3',
#         'perk4', 'perk4Var1', 'perk4Var2', 'perk4Var3',
#         'perk5', 'perk5Var1', 'perk5Var2', 'perk5Var3',
#         'perkPrimaryStyle',
#         'perkSubStyle',
#         'statPerk1', 'statPerk2'
#         ]
#     for key in range(len(props)):
#         perk_id = props[key]
#         match[perk_id] = process_perk_data(match[perk_id])

#     props = [
#         'championId'
#     ]
#     for key in range(len(props)):
#         champ_id = props[key]
#         match[champ_id] = process_champion_data(match[champ_id])

#     props = [
#         'spell1Id',
#         'spell2Id'
#     ]
#     for key in range(len(props)):
#         spell_id = props[key]
#         match[spell_id] = process_spell_data(match[spell_id])

# # perform write operation
# for match in writeableq:
#     to_csv(match, 'write_qual_pro.csv')
