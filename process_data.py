
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
df = pd.read_csv('write.csv')

# perform kmeans
clusters, df_reduced = kmeans(N_CLUSTERS, df)

print("............................................back to main file............................................")

# to have a look
for i, c in enumerate(clusters):
    subdf = df_reduced[df_reduced['cluster'] == i]
    print('cluster ', i)
    print('number of players in cluster: ', len(subdf))
    print(clusters[i]) # <<< clusters to use
    print(clusters[i].columns)

    # merge cluster on qualitative values 

# ======= to consider to have some irrelevant graphs on pro players ========
# for players that get dropped from roster: visualize how a player changes over time, what does their performance look like until they get dropped from the roster?
# does side affect how the player acts?

##### > select based on ROLE [after WIP], to classify players based on ROLE (since TOP will have diff stats from SUPP, etc.)**



### reccomendation system useing kmeans -> collaborative filtering
# find cluster user is in
def cluster_with_user(user):
    pass

# find similar in cluster
def reccommendation_for_similar_user(cluster, user):
    pass

## print top 5 recommendations