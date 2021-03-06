
import pandas as pd
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from kmeans import kmeans

# pandas options
# pd.set_option('display.max_rows', 500)

N_CLUSTERS = 5

df_quant = pd.read_csv('write_quant_pro.csv')
df_qual = pd.read_csv('write_qual_pro.csv')

# perform kmeans
clusters, df_clusters = kmeans(N_CLUSTERS, df_quant, df_qual) # quantatitive values, all values

print("............................................back to main file............................................")

# cluster commonality - for role score
commonality = {}

# cluster data
clusterqs = [] # qualitative
for i, c in enumerate(clusters):
    print('cluster ', i, 'number of players in cluster: ', len(clusters[i]))
    # clusters[i] = clusters[i].dropna(axis=1, how='all')

    # qualitative
    subdf_qual = df_clusters[df_clusters['cluster'] == i]
    subdf_qual = subdf_qual.merge(df_qual, on="summonerName", how = 'left')
    print(subdf_qual)
    clusterqs.append(subdf_qual)

    # create row commonality rankings { ROLE: 1, ROLE: 0.5, ROLE: 0.0, ROLE: -0.5, ROLE: -1.0 } for calculating the role score
    # example (for all 5 roles existing in cluster)
    # commonality[i] = {
    #     rolestats[0]: 1.0,
    #     rolestats[1]: 0.5,
    #     rolestats[2]: 0.0,
    #     rolestats[3]: -0.5,
    #     rolestats[4]: -1.0
    # }
    rolestats = subdf_qual['lane'].value_counts().index.tolist()
    decrement_factor = 2.0 / (len(rolestats) - 1)
    weight = 1.0
    icommon = {}
    for j in range(len(rolestats)): 
        # commonality[i][j] = weight
        icommon[rolestats[j]] = weight
        weight -= decrement_factor
    commonality[i] = icommon

    ### SOME BASIC CLUSTER STATS
    # role played
    # print(clusters[i]["role"].value_counts())

    # lane played
    # print(clusters[i]["lane"].value_counts())
    
    # print(clusters[i].mean())

    # common spells taken
    # spelldf_lst = clusters[i]['spell1Id'].to_list() + clusters[i]['spell2Id'].to_list()
    # spelldf = pd.DataFrame({'spells': spelldf_lst })
    # print(spelldf.value_counts())

    print()

print(commonality)
# ======= to consider to have some irrelevant graphs on pro players ========
# for players that get dropped from roster: visualize how a player changes over time, what does their performance look like until they get dropped from the roster?
# does side affect how the player acts?

##### > select based on ROLE [after WIP], to classify players based on ROLE (since TOP will have diff stats from SUPP, etc.)**

#####################################################################################################################################################################################
# see paper
figure1 = pd.DataFrame()

# map each player to its league
def tournament_mappings(df):
    pro_map = {}
    team_mapping = df[['league', 'player', 'team']]
    for league in df['league'].unique():
        leaguedict = []
        leaguedf = team_mapping[team_mapping['league'] == league]
        for team in leaguedf['team'].unique(): 
            teamdf = leaguedf[leaguedf['team'] == team]
            leaguedict.append({str(team): teamdf['player'].unique().tolist()})

        pro_map[league] = leaguedict
    return pro_map

pro_tournaments_teams = tournament_mappings(pd.read_csv('league_pro_matches_data/2019-spring-match.csv'))
tournamentlist = []
teamslist = []
tournamentplayerct = []
net_accuracy = []
net_role_error = []
for tournament in pro_tournaments_teams.keys():
    totalNoPlayers = 0
    tournamentlist.append(tournament)

    teams = []
    for team in pro_tournaments_teams[tournament]:
        key, value = list(team.items())[0]
        totalNoPlayers += len(value)
        teams.append(key)
    
    # find cluster user is in
    def cluster_with_user(user, df_clusters):
        return df_clusters.loc[df_clusters.index == user]['cluster']
    # print('cluster ', cluster_with_user('C9 VULCAN', clusters)[0]) # example

    # evaluate accuracy / role error for each team here
    team_roster = pro_tournaments_teams[tournament]

    accuracy = 0
    role_err = 0
    count = 0
    for team in team_roster:
        team_name, team_roster = list(team.items())[0]

        roster_classes = []
        for memb in team_roster:
            # catching the weird team stats in the csvs
            if memb == 'Team': 
                continue

            clust = cluster_with_user(memb, df_clusters)
            clust = clust.to_list()

            # is there an assigned cluster?
            if len(clust) > 0:
                roster_classes.append(clust[0])
            else:
                roster_classes.append(None)

        # needs to be more than 1; if only 1 element, will never overlap
        none_removed = [x for x in roster_classes if x is not None]
        if len(none_removed) > 1:
            # print(team_roster)
            # print(roster_classes)

            # evaluate accuracy
            accuracy += float(len(set(none_removed)) / len(none_removed))

            # [TODO] evaluate each member's role error (using commonality dict)
            # negative is off from correct result, positive is correctness
            for ind in range(len(team_roster) - 1):
                user = team_roster[ind]
                cluster = roster_classes[ind]
                # print(user, cluster)

                # calculate role error for each memb being evaluated, add avg to role_err
                if cluster is not None:
                    # print(commonality[cluster])
                    membdf = clusterqs[cluster][['summonerName', 'lane', 'cluster']]
                    membdf = membdf[membdf['summonerName'] == user]
                    membdf = membdf['lane'].value_counts()
                    membdf = membdf.to_dict()

                    subrole_err = 0
                    count_err = 0
                    for membrole in membdf:
                        # print(membrole, membdf[membrole])
                        subrole_err += commonality[cluster][membrole] * membdf[membrole]
                        count_err += membdf[membrole]
                    if count_err > 0:
                        role_err += float(subrole_err) / count_err

                # average out on line 158

            count += 1

    tournamentAcc = accuracy / count
    net_accuracy.append(tournamentAcc)
    net_role_error.append(role_err / count)

    print(','.join(teams))
    teamslist.append(','.join(teams))

    tournamentplayerct.append(totalNoPlayers)

# see paper
figure1['Tournament'] = tournamentlist
figure1['Teams'] = teamslist
figure1['No. of Players'] = tournamentplayerct
figure1['Accuracy'] = net_accuracy
figure1['Role Error'] = net_role_error
    
print(figure1)
#####################################################################################################################################################################################

