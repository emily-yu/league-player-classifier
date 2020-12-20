
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

# to have a look @ cluster data (with both qual and quant data)
for i, c in enumerate(clusters):
    print('cluster ', i, 'number of players in cluster: ', len(clusters[i]))
    clusters[i] = clusters[i].dropna(axis=1, how='all')

    ### SOME BASIC CLUSTER STATS
    # role played
    # print(clusters[i]["role"].value_counts())

    # lane played
    # print(clusters[i]["lane"].value_counts())
    
    print(clusters[i].mean())

    # common spells taken
    # spelldf_lst = clusters[i]['spell1Id'].to_list() + clusters[i]['spell2Id'].to_list()
    # spelldf = pd.DataFrame({'spells': spelldf_lst })
    # print(spelldf.value_counts())

    print()

# ======= to consider to have some irrelevant graphs on pro players ========
# for players that get dropped from roster: visualize how a player changes over time, what does their performance look like until they get dropped from the roster?
# does side affect how the player acts?

##### > select based on ROLE [after WIP], to classify players based on ROLE (since TOP will have diff stats from SUPP, etc.)**



### reccomendation system useing kmeans -> collaborative filtering

# find similar in cluster
def reccommendation_for_similar_user(cluster, user):
    pass

## print top 5 recommendations