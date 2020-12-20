# league-player-classifier

In professional gaming, team compositions are crafted carefully to ensure that players are of the highest skill level compatible with each other. However, the process by which players are able to work together, in both professional and non-professional gameplay, leaves room for exploration. In this paper, we use game data sourced directly from League of Legends to analyze similarities between ranked gameplay to gain insight on whether archetypes exist in professional and non-professional gaming.

For an extremely rather shoddy explanation of this work written at ungodly hours, please reference the following [paper](docs/league of legumes_  pros vs challenjour (1).pdf) or [presentation](docs/league of legumes_  pros vs challenjour.pptx). 

## Usage

Install all requirements from `requirements.txt` using `pip install requirements.txt`. 

### Functions: 

1. [To perform a fresh analysis of the data...](#fresh-analysis)
2. [To run the generation file to pull new data from the Riot API...](#new-data)


## Repository Architecture

### **Directories**  

```
/cdragon_en_US
```
Data pulled directly from [CommunityDragon](https://www.communitydragon.org/) or CDragon, the Riot Developer API's static data. Downloaded 10.25.1, the latest version on 12/18/20. 

- `summoner.json`; utilitzed in data analysis for conversion of numerical spell keys to qualitative data
- `item.json`; utilitzed in data analysis for conversion of numerical item keys to qualitative data of item name

```
/data
```
Data pulled directly from [Kaggle](https://www.kaggle.com/gyejr95/league-of-legendslol-ranked-games-2020-ver1), for referencing non-professional games/players to send to the Riot API itself. 

```
/docs
```
Contains misc. files that were used for brainstorming and more recent submissions, as well as for writing documentation.

```
/league_pro_matches_data
```
Data pulled directly from [Kaggle](https://www.kaggle.com/huitongkou/league-of-legends-pro-matches-data). Manually transformed `2019-spring-match-data-OraclesElixir-2019-05-21.xlsx` into a `.csv` for processing on the development side. 

### **Executable Files**

Files prefixed with a `_pro` refer to utility related to professional player data, and those without or with a `_challenger` refer to non-professional player data.
```
kmeans.py
```
Performs the k-means clustering algorithm. Imported into `process_data_pro.py` and `process_data.py`.


```
process_data_pro.py
```
```
process_data.py
```
Analyzes the csv data generated from to `riot_to_csv...` files below. Performs the following:
 
- clustering
- reading of input files; csvs
- data transformation (merging of dataframes)
- writes the clustered/elbow figures as shown in the docs
- generates the table values as shown in the docs

#### To perform a fresh analysis of the data: <a name="fresh-analysis"></a>

1. Ensure that the data in all `write_qual...` files are populated. By default, they should be populated, but executing the `riot_to_csv` files wrongly can wipe them. 
2. Run `python process_data_pro.py` or `python process_data.py`.
3. View the console for data being printed out.

```
riot_to_csv_pro.py
```
```
riot_to_csv.py
```
Performs call to Riot API to generate csv files. 

- `riot_to_csv_pro.py` correlates to `_pro.csv` util files
- `riot_to_csv.py` correlates to `_challenger.csv` files

**To run the generation file:** <a name="new-data"></a>
*Note: requires a verified League of Legends account! For demo purposes, I am able to only provide a key that lasts for 24h, please reach out in the case of assistance.*

1. Log onto account at [Riot Games Developer Portal](https://developer.riotgames.com/)
2. Go to Dashboard, and look for Development API Key section. 
3. Generate API key by clicking Regenerate API key. Save this somewhere for the next step. 
4. Execute file: `python3 riot_to_csv_pro.py` or `python3 riot_to_csv.py`
5. The file will prompt for you to enter your API key - enter it from step 3. 
6. The file will run for a very long duration of time. When complete, the previous .csv file in the respective expected location will be overwritten with fresh data. 

**To shorten the execution time length for demo/testing purposes:** 
> otherwise, may take upwards of 5 hours to finish executing, but no worries - contains rate limiting accomodations so no monitoring needed

`riot_to_csv_pro.py`: 

1. Line 27: Set `MAX_MATCHES` to a smaller number (ex. 2) 

`riot_to_csv.py`: 

1. Line 11: Set `PLAYER_LIMIT` to smaller number, or alternatively uncomment Line 10. 
2. Line 70: Set `MAX_MATCHES` to a smaller number (ex. 2)


### **Utility**

```
write_qual_challenger.csv
```
```
write_quant_challenger.csv
```
Contains data on challenger/grandmaster/master players using players referenced from [this dataset.](https://www.kaggle.com/gyejr95/league-of-legendslol-ranked-games-2020-ver1) Analysis performed completely separate due to lack of data and effort needed to transform data to match Riot API data, because no comprehensive non-pro dataset. Generated from `riot_to_csv.py`.

Data is separated into two .csv files: 

1. Files containing the stub `_qual` contain qualitative data, so the following features in the scrollable code block below. 
>
```
summonerName,item0,item1,item2,item3,item4,item5,item6,perk0,perk0Var1,perk0Var2,perk0Var3,perk1,perk1Var1,perk1Var2,perk1Var3,perk2,perk2Var1,perk2Var2,perk2Var3,perk3,perk3Var1,perk3Var2,perk3Var3,perk4,perk4Var1,perk4Var2,perk4Var3,perk5,perk5Var1,perk5Var2,perk5Var3,perkPrimaryStyle,perkSubStyle,statPerk1,statPerk2,championId,spell1Id,spell2Id,role,lane
```

2. Files containing the stub `_quant` contain quantitative data, so the following features in the scrollable code block below. 
>
```
summonerName,win,kills,deaths,assists,largestKillingSpree,largestMultiKill,killingSprees,longestTimeSpentLiving,doubleKills,tripleKills,quadraKills,pentaKills,unrealKills,totalDamageDealt,magicDamageDealt,physicalDamageDealt,trueDamageDealt,largestCriticalStrike,totalDamageDealtToChampions,magicDamageDealtToChampions,physicalDamageDealtToChampions,trueDamageDealtToChampions,totalHeal,totalUnitsHealed,damageSelfMitigated,damageDealtToObjectives,damageDealtToTurrets,visionScore,timeCCingOthers,totalDamageTaken,magicalDamageTaken,physicalDamageTaken,trueDamageTaken,goldEarned,goldSpent,turretKills,inhibitorKills,totalMinionsKilled,neutralMinionsKilled,neutralMinionsKilledTeamJungle,neutralMinionsKilledEnemyJungle,totalTimeCrowdControlDealt,champLevel,visionWardsBoughtInGame,sightWardsBoughtInGame,wardsPlaced,wardsKilled,firstBloodKill,firstBloodAssist,firstTowerKill,firstTowerAssist,firstInhibitorKill,firstInhibitorAssist,creepsPerMinDeltas0-10,creepsPerMinDeltas10-20,creepsPerMinDeltas20-30,xpPerMinDeltas0-10,xpPerMinDeltas10-20,xpPerMinDeltas20-30,goldPerMinDeltas0-10,goldPerMinDeltas10-20,goldPerMinDeltas20-30,xpDiffPerMinDeltas0-10,xpDiffPerMinDeltas10-20,xpDiffPerMinDeltas20-30,damageTakenPerMinsDeltas0-10,damageTakenPerMinsDeltas10-20,damageTakenPerMinsDeltas20-30,damageTakenDiffPerMinsDeltas0-10,damageTakenDiffPerMinsDeltas10-20,damageTakenDiffPerMinsDeltas20-30
```

```
write_qual_pro.csv
```
```
write_quant_pro.csv
```
Contains data generated from `riot_to_csv_pro.py`, rows contain data from Spring 2019 Tournament Matches. See above for naming conventions. 

### **Archive**

```
wip.txt
```
```
wip_submission.zip
```
The above is an archive of my submissions for milestone checkins. 


```
/archive_ipynbs
```
Previous work that was used before migration to standard `.py` files, as `.ipynb` files do not register well with Git. 