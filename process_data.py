
import pandas as pd
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from kmeans import kmeans

N_CLUSTERS = 5

# df = pd.read_csv('oldwriteto.csv')
# df = pd.read_csv('write.csv')
df_quant = pd.read_csv('write_quant.csv')
df_qual = pd.read_csv('write_qual.csv')

# perform kmeans
clusters = kmeans(N_CLUSTERS, df_quant, df_qual)

print("............................................back to main file............................................")

# to have a look @ cluster data (with both qual and quant data)
for i, c in enumerate(clusters):
    print('cluster ', i, 'number of players in cluster: ', len(clusters[i]))

# ======= to consider to have some irrelevant graphs on pro players ========
# for players that get dropped from roster: visualize how a player changes over time, what does their performance look like until they get dropped from the roster?
# does side affect how the player acts?

##### > select based on ROLE [after WIP], to classify players based on ROLE (since TOP will have diff stats from SUPP, etc.)**



### reccomendation system useing kmeans -> collaborative filtering
# find cluster user is in
def cluster_with_user(user, clusters):
    for ind, cluster in enumerate(clusters):
        names = cluster['summonerName'].tolist()
        if user in names:
            return (ind, cluster)
    return None

print('cluster ', cluster_with_user('C9 VULCAN', clusters)[0]) # example

# find similar in cluster
def reccommendation_for_similar_user(cluster, user):
    pass

## print top 5 recommendations