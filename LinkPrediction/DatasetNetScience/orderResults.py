import time
import numpy as np
import pandas as pd
import pickle
import gc
import networkx as nx

G = nx.read_gml('GeneratedData/testNetScience.gml')
Gset_edges = set(G.edges())

print(len(Gset_edges))
np.set_printoptions(precision=7)
np.set_printoptions(suppress=True)

path = 'GeneratedData/mp_lp_alg_resultsDefinitive.txt'
textLength = 0
firstLine = True
with open(path) as lines:
    for line in lines:
        if firstLine:
            firstLine = False
            continue
        else:
            textLength += 1

cnList = np.empty((textLength,9))


firstLine = True
i = 0
count = 0
start = time.time()
with open(path) as lines:
    for line in lines:
        if firstLine:
            firstLine = False
            continue
        else:
            #print(cnList[i])
            splitLine = line.split(',')
            if tuple((splitLine[0], splitLine[1])) not in Gset_edges:
                cnList[i] = [int(splitLine[0]),int(splitLine[1]),int(splitLine[2]),splitLine[3],int(splitLine[4]),splitLine[5],splitLine[6],splitLine[7].strip('\n'),0.0]
            else:
                count += 1
                cnList[i] = [int(splitLine[0]),int(splitLine[1]),int(splitLine[2]),splitLine[3],int(splitLine[4]),splitLine[5],splitLine[6],splitLine[7].strip('\n'),1.0]
            #print(cnList[i])
            i += 1

#cnList.sort(key = lambda i: i[2], reverse=True)
#cnListsorted = cnList[cnList[:, 2].argsort()[::-1]]
#print(max,min)
print(count)

# Create the dataframe
df = pd.DataFrame(cnList,columns=['Node1', 
                      'Node2', 'CN', 'JaccardCoefficient', 'PrefAttachment', 'AdamicAdar', 'QCNJacCoeff', 'QCNAdamicA', 'IsTestSet'])

df['Node1'] = df['Node1'].astype(int)
df['Node2'] = df['Node2'].astype(int)
df['CN'] = df['CN'].astype(int)
df['PrefAttachment'] = df['PrefAttachment'].astype(int)
df['IsTestSet'] = df['IsTestSet'].astype(int)

df.to_pickle("GeneratedData/DataFrameNetScience.pkl")

#df = pd.read_pickle("./dummy.pkl")