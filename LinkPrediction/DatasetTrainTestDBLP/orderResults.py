import time
import numpy as np
import pandas as pd
import pickle
import gc

G = pickle.load(open('GeneratedData/GTestIndexedWithLabel.pkl', 'rb'))
Gset_edges = set(G.edges())

del G
gc.collect()

np.set_printoptions(precision=6)
np.set_printoptions(suppress=True)
path = 'GeneratedData/mp_cn_alg_results.txt'
textLength = 0
firstLine = True
with open(path) as lines:
    for line in lines:
        if firstLine:
            firstLine = False
            continue
        else:
            textLength += 1

cnList = np.empty((textLength,6))


firstLine = True
i = 0
start = time.time()
with open(path) as lines:
    for line in lines:
        if firstLine:
            firstLine = False
            continue
        else:
            #print(cnList[i])
            splitLine = line.split(', ')
            if tuple((int(splitLine[0]), int(splitLine[1]))) not in Gset_edges:
                cnList[i] = [int(splitLine[0]),int(splitLine[1]),int(splitLine[2]),splitLine[3],splitLine[4].strip('\n'),0.0]
            else:
                cnList[i] = [int(splitLine[0]),int(splitLine[1]),int(splitLine[2]),splitLine[3],splitLine[4].strip('\n'),1.0]
                Gset_edges.remove(tuple((int(splitLine[0]), int(splitLine[1]))))
            #print(cnList[i])
            i += 1

#cnList.sort(key = lambda i: i[2], reverse=True)
#cnListsorted = cnList[cnList[:, 2].argsort()[::-1]]
#print(max,min)

del Gset_edges
gc.collect()

# Create the dataframe
df = pd.DataFrame(cnList,columns=['Node1', 
                      'Node2', 'CN', 'JaccardCoefficient', 'AdamicAdar', 'IsTestSet'])

df['Node1'] = df['Node1'].astype(int)
df['Node2'] = df['Node2'].astype(int)
df['CN'] = df['CN'].astype(int)
df['IsTestSet'] = df['IsTestSet'].astype(int)

df.to_pickle("GeneratedData/DataFrame.pkl")

#df = pd.read_pickle("./dummy.pkl")