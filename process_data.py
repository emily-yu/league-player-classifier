
import pandas as pd
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import json
from kmeans import kmeans

# utility
def pj(inp):
    print(json.dumps(inp, indent=2))

# pandas options
pd.set_option('display.max_rows', 500)

N_CLUSTERS = 5

df_quant = pd.read_csv('write_quant.csv')
df_qual = pd.read_csv('write_qual.csv')

# perform kmeans
clusters, df_clusters = kmeans(N_CLUSTERS, df_quant, df_qual)

print("............................................back to main file............................................")

# cluster commonality - for role score
commonality = {}

# figure data
df_clusterno = []
df_playercount = []
df_roleerror = []

# cluster data
clusterqs = [] # qualitative
for i, c in enumerate(clusters):
    print('cluster ', i, 'number of players in cluster: ', len(clusters[i]))
    df_clusterno.append(i)

    removed = clusters[i][clusters[i]['win'] < 0.19].index.to_list()  # wr must be greater than 0.2
    print(removed)
    # clusters[i] = clusters[i].dropna(axis=1, how='all')

    # qualitative
    subdf_qual = df_clusters[df_clusters['cluster'] == i]
    inds = subdf_qual[ subdf_qual.index.isin(removed) ].index # drop values that are in list to remove
    subdf_qual.drop(inds, inplace=True)
    subdf_qual = subdf_qual.merge(df_qual, on="summonerName", how = 'left') # merge qualitative values into summoners
    print(subdf_qual)
    clusterqs.append(subdf_qual)
    df_playercount.append(len(subdf_qual))

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

    print(commonality)

    accuracy = 0
    role_err = 0
    count = 0

    # role error for cluster
    subdf_qual['laneval'] = subdf_qual['lane'].map(commonality[i])
    role_err = subdf_qual['laneval'].mean()
    df_roleerror.append(role_err)

    # accuracy
    playerlist = subdf_qual['summonerName'].unique()
    for player in playerlist:
        playerdf = subdf_qual[subdf_qual['summonerName'] == player]
        accepted = playerdf.value_counts('lane')[:2]
        # print(player, accepted)

figure2 = pd.DataFrame()
figure2['Cluster'] = df_clusterno
figure2['Player Count'] = df_playercount
figure2['Role Error'] = df_roleerror

print(figure2)