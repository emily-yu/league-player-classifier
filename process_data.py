
import pandas as pd
# df = pd.read_csv('write.csv')
# print(df)







import pickle
# with open('data/match_data_version1.pickle', 'rb') as fid:
#      data3 = pickle.load(fid)
#      print('Data After  Read :', data3)

# data3

print("helo")

# import xlrd
# !pip install xlrd
import pandas as pd

# df = pd.read_excel('league_pro_matches_data/2019-spring-match-data-OraclesElixir-2019-05-21.xlsx')
df = pd.read_csv('write.csv')
# df

# analyze per roles, since each role is played differently / has different goals and purpose within game
# each player should generally stick to their own role on their own team, so analyze per PRO PLAYER within ROLE
# top = df.loc[df['position'] == 'Top']
# print("TOP DF")
# top

# mid = df[df['position'] == 'Middle']
# print("MID DF")
# print(mid)

# sup = df[df['position'] == 'Support']
# print("SUPPORT DF")
# print(sup)

# adc = df[df['position'] == 'ADC']
# print(adc)

# jg = df[df['position'] == 'Jungle']
# print(jg)

'''
random notes
- for number comparisons, get average of all PRO data and see how PLAYER data compares

qualitative cols
- champion pool (get over ALL games)
- ban pool (ban1, ban2, ban3, ban4, ban5)
    pick top 5 most common bans over ALL games

quantitative cols
- average win rate (result)
    if average wr > 0.5, consider as winning player
- kda ratio comparison (in terms of relative team contribution)
- 

cols: 
- doubles, triples, quadras, pentas
- fb (first blood)
    - fbassist (first blood assist)
    - fbvictim (first blood victim)
    - fbtime (first blood time)
- kpm (kills per min)
    - okpm
    - ckpm (creep kills per min)
- fd (first death)
    - fdtime (first death time)
- for objective control...
    - teamdragkill
    - oppdragkill
    - elementals
    - oppelemental
    - firedrake
    - waterdrake
    - earthdrake
    - airdrakes
    - elders
    - oppelders
    - herald
    - heraldtime
- ft (first tower)
    - fttime
- firstmid
- firstmidouter
- firsttothreetowers
- teamtowerkills
- opptowerkills
- fbaron
- fbarontime
- teambaronkills
- oppbaronkills
- dmgtochamps
- dmgtochampsperminute
- dmgshare
- earnedgoldshare
- wards
- wpm
- wardshare
- wardkills
- wcpm
- visionwards
- visionwardbuys
- visiblewardclearrate
- invisiblewardclearrate
- totalgold
- earnedgpm
- goldspent
- gspd
- minionkills
- monsterkills
- monsterkillsownjungle
- monsterkillsenemyjungle
- cspm
- goldat10
- oppgoldat10
- gdat10
- goldat15
- oppgoldat15
- gdat15
- xpat10
- oppxpat10
- xpdat10
- csat10
- oppcsat10
- csdat10
- csat15
- oppcsat15
- csdat15

for extension: average game length (use for game comparisons)
    to find which pro game would be most similar
    to try and pick a winning team, pick similar normal players to the PRO non-aggregate row values
        [tbd]
'''
# ======= to consider to have some irrelevant graphs on pro players ========
# for players that get dropped from roster: visualize how a player changes over time, what does their performance look like until they get dropped from the roster?
# does side affect how the player acts?

# remove irrelevant columns
# df.drop(columns=['gameid', 'url', 'league', 'split', 'date', 'week', 'patchno', 'side', 'playerid', 'game'], axis=1, inplace=True)

# Commented out IPython magic to ensure Python compatibility.
# KEY STEPS (number one priority)

##### > select based on ROLE [after WIP], to classify players based on ROLE (since TOP will have diff stats from SUPP, etc.)**
##### > average out data of each pro player for kmeans
# avgs = df.groupby('player').mean()
avgs = df.groupby('summonerName').mean()
print(avgs.columns)
print("avgs")
print(avgs)
avgs = avgs.fillna(0)


##### > create kmenas clusters for QUANTIATIVE VALUES [TODO] 
# ...fill any values with averages of all players to make sure no missing values https://www.datacamp.com/community/tutorials/k-means-clustering-python
# ...all numerical values because good for quantative values
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import MinMaxScaler
# !pip3 install seaborn
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

# ref https://datascience.stackexchange.com/questions/16700/confused-about-how-to-apply-kmeans-on-my-a-dataset-with-features-extracted
# kmeans = KMeans(n_clusters=2) # number of clusters
# kmeans.fit(X)

# KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
#     n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
#     random_state=None, tol=0.0001, verbose=0)

# # X = np.array(train.drop(['Survived'], 1).astype(float))
# X = np.array(avgs)
# correct = 0
# for i in range(len(X)):
#     predict_me = np.array(X[i].astype(float))
#     predict_me = predict_me.reshape(-1, len(predict_me))
#     prediction = kmeans.predict(predict_me)
#     if prediction[0] == y[i]:
#         correct += 1

# print(correct/len(X))
'''
#Cluster the data
kmeans = KMeans(n_clusters=5, random_state=0).fit(avgs)
labels = kmeans.labels_

centroids = kmeans.cluster_centers_
print("cnetrodis: ")
print(centroids)

#Glue back to originaal data
avgs['clusters'] = labels

#Add the column into our list
# clmns.extend(['clusters'])

#Lets analyze the clusters
print(avgs[:].groupby(['clusters']).mean())
#Scatter plot of Wattage and Duration
sns.lmplot('k', 'd', 
           data=avgs, 
           fit_reg=False, 
           hue="clusters",  
           scatter_kws={"marker": "D", 
                        "s": 100})
plt.title('Clusters Kills vs Deahts')
plt.xlabel('Kills')
plt.ylabel('Deaths')'''

# #3 Using the elbow method to find out the optimal number of #clusters. 
# #KMeans class from the sklearn library.
# # from sklearn.cluster import KMeans
# X = avgs
# wcss=[]
# #this loop will fit the k-means algorithm to our data and 
# #second we will compute the within cluster sum of squares and #appended to our wcss list.
# for i in range(1,len(avgs.columns)): 
#      kmeans = KMeans(n_clusters=i, init ='k-means++', max_iter=300,  n_init=len(avgs.columns),random_state=0 )
# #i above is between 1-10 numbers. init parameter is the random #initialization method  
# #we select kmeans++ method. max_iter parameter the maximum number of iterations there can be to 
# #find the final clusters when the K-meands algorithm is running. we #enter the default value of 300
# #the next parameter is n_init which is the number of times the #K_means algorithm will be run with
# #different initial centroid.
# kmeans.fit(X)
# #kmeans algorithm fits to the X dataset
# print("................")
# print(kmeans)
# print(kmeans.inertia_)
# wcss.append(kmeans.inertia_)
# #kmeans inertia_ attribute is:  Sum of squared distances of samples #to their closest cluster center.
# #4.Plot the elbow graph
# plt.plot(range(1,len(avgs.columns)),wcss)
# plt.title('The Elbow Method Graph')
# plt.xlabel('Number of clusters')
# plt.ylabel('WCSS')
# plt.show() # ['stopped here'] https://medium.com/pursuitnotes/k-means-clustering-model-in-6-steps-with-python-35b532cfa8ad <<<<<<<<<<<<<<<<<<<<

# for QUALITATIVE VALUES [bans, champs]: 
# https://stackoverflow.com/questions/14720324/compute-the-similarity-between-two-lists
# print("players: ", df.player.unique()) # players to pull qual data for
# print("number of players: ", len(df.player.unique())) # players to pull qual data for

# print("QUAL DATA")
# champion_pool = bwipo['champion'].value_counts()
# print('champion pool :')
# print(champion_pool)

# roles = bwipo['position'].value_counts() # for funs
# print('roles :')
# print(champion_pool)

# ban_pool = bwipo[['ban1', 'ban2', 'ban3', 'ban4', 'ban5']] # not player specific, but player probably has some input; can use to calculate champion ban frequency against champions in player if bored, [irrelevant]
# print(ban_pool)

##### > average between quantatative and qualitative values to consider all elements in data
# ( for game analysis, only use bans, as player's champ they played that game / want to play that game is picked by the player. alternatively, can do reverse analysis picks for what champion to play )

# k means implementation from: https://github.com/OpenClassrooms-Student-Center/Multivariate-Exploratory-Analysis/blob/master/3a.%20K-Means%20Clustering.ipynb

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def display_factorial_planes(X_projected, n_comp, pca, axis_ranks, labels=None, alpha=1, illustrative_var=None):
    '''Display a scatter plot on a factorial plane, one for each factorial plane'''

    # For each factorial plane
    for d1,d2 in axis_ranks:
        if d2 < n_comp:
 
            # Initialise the matplotlib figure      
            fig = plt.figure(figsize=(7,6))
        
            # Display the points
            if illustrative_var is None:
                plt.scatter(X_projected[:, d1], X_projected[:, d2], alpha=alpha)
            else:
                illustrative_var = np.array(illustrative_var)
                for value in np.unique(illustrative_var):
                    selected = np.where(illustrative_var == value)
                    plt.scatter(X_projected[selected, d1], X_projected[selected, d2], alpha=alpha, label=value)
                plt.legend()

            # Display the labels on the points
            if labels is not None:
                for i,(x,y) in enumerate(X_projected[:,[d1,d2]]):
                    plt.text(x, y, labels[i],
                              fontsize='14', ha='center',va='center') 
                
            # Define the limits of the chart
            boundary = np.max(np.abs(X_projected[:, [d1,d2]])) * 1.1
            plt.xlim([-boundary,boundary])
            plt.ylim([-boundary,boundary])
        
            # Display grid lines
            plt.plot([-100, 100], [0, 0], color='grey', ls='--')
            plt.plot([0, 0], [-100, 100], color='grey', ls='--')

            # Label the axes, with the percentage of variance explained
            plt.xlabel('PC{} ({}%)'.format(d1+1, round(100*pca.explained_variance_ratio_[d1],1)))
            plt.ylabel('PC{} ({}%)'.format(d2+1, round(100*pca.explained_variance_ratio_[d2],1)))

            plt.title("Projection of points (on PC{} and PC{})".format(d1+1, d2+1))
            #plt.show(block=False)
   
# Standardize the data
X = avgs
scaler = StandardScaler()
X_scaled = scaler.fit_transform(avgs)

df_X_scaled = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)
# print(df_X_scaled.loc[df_X_scaled.index == 'Team'])
df_X_scaled.drop(df_X_scaled.loc[df_X_scaled.index=='True'].index, inplace=True)

print(X.columns, X.index)
print('X_scaled')
print(X_scaled)
print('df_X_scaled.head()')
print(df_X_scaled)
# print(df_X_scaled.head())

# create and fit data for model
kmeans = KMeans(init='random', n_clusters=3, n_init=10)
kmeans.fit(X_scaled)

# Determine which clusters each data point belongs to:
clusters = kmeans.predict(X_scaled)
print('clusters')
print(clusters)

# Add cluster number to the original data
X_scaled_clustered = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)
X_scaled_clustered['cluster'] = clusters

print('X_scaled_clustered.head()')
print(X_scaled_clustered.head())

# Run a number of tests, for 1, 2, ... num_clusters
num_clusters = 50
kmeans_tests = [KMeans(n_clusters=i, init='random', n_init=10) for i in range(1, num_clusters)]
score = [kmeans_tests[i].fit(X_scaled).score(X_scaled) for i in range(len(kmeans_tests))]

# Plot the curve
plt.plot(range(1, num_clusters),score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()

# plotting the clusters (again pulled from above link)
from sklearn.decomposition import PCA

# data into 2d (x, y) for plotting
pca = PCA(n_components=2)
pca.fit(X_scaled)
X_reduced = pca.transform(X_scaled)

# Convert to a data frame
X_reduceddf = pd.DataFrame(X_reduced, index=X.index, columns=['PC1','PC2'])
X_reduceddf['cluster'] = clusters
print('X_reduceddf.head()')
print(X_reduceddf.head())
print(X_reduceddf)

print(kmeans.cluster_centers_)
centres_reduced = pca.transform(kmeans.cluster_centers_)

display_factorial_planes(X_reduced, 2, pca, [(0,1)], illustrative_var = clusters, alpha = 0.8)
plt.scatter(centres_reduced[:, 0], centres_reduced[:, 1],
            marker='x', s=169, linewidths=3,
            color='k', zorder=10)

# USAGE AGAINST A NORMAL PLAYER [TODO]
# select columns of data to be compared (data existing for the pro player data set)
# calculate cosine_similarity between PLAYER and all other PRO player aggregate stats in their role
# select the most similar / greatest cosine_similarity value and claim that that is the most similar PRO player

N_CLUSTERS = 3
clusters = [X_scaled[clusters == i] for i in range(N_CLUSTERS)]
df = X_reduceddf
# to have a look
for i, c in enumerate(clusters):
    subdf = df[df['cluster'] == i]
    print('cluster ', i)
    print('number of players in cluster: ', len(subdf))
    df_with_clusters = subdf.merge(avgs, how='left', left_index=True, right_index=True)
    print(df_with_clusters) # <<< clusters to use
    print(df_with_clusters.index.tolist())