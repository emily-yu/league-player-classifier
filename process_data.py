
import pandas as pd
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

N_CLUSTERS = 5

# df = pd.read_csv('oldwriteto.csv')
df = pd.read_csv('write.csv')

# ======= to consider to have some irrelevant graphs on pro players ========
# for players that get dropped from roster: visualize how a player changes over time, what does their performance look like until they get dropped from the roster?
# does side affect how the player acts?

##### > select based on ROLE [after WIP], to classify players based on ROLE (since TOP will have diff stats from SUPP, etc.)**

##### > average out data of each pro player for kmeans
avgs = df.groupby('summonerName').mean()
print(avgs.columns)
print("avgs")
print(avgs)
avgs = avgs.fillna(0)


##### create kmenas clusters for QUANTIATIVE VALUES
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
kmeans = KMeans(init='random', n_clusters=N_CLUSTERS, n_init=10)
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
plt.show()

# USAGE AGAINST A NORMAL PLAYER [TODO]
# select columns of data to be compared (data existing for the pro player data set)
# calculate cosine_similarity between PLAYER and all other PRO player aggregate stats in their role
# select the most similar / greatest cosine_similarity value and claim that that is the most similar PRO player

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