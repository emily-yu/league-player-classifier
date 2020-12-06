import pickle
with open('data/match_data_version1.pickle', 'rb') as fid:
     data3 = pickle.load(fid)
     print('Data After  Read :', data3)