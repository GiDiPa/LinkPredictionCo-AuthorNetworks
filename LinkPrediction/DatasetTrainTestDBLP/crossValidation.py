import numpy as np
import pandas as pd
import sklearn.metrics
import pickle
import matplotlib.pyplot as plt
import networkx as nx
import math
import gc


G = pickle.load(open('GeneratedData/GTestIndexedWithLabel.pkl', 'rb'))
lenGset_edges = len(set(G.edges()))
print(lenGset_edges)



#pd.DataFrame(cnList,columns=['Node1', 
                      #'Node2', 'CN', 'JaccardCoefficient', 'AdamicAdar', 'IsTestSet'])

ranking = pd.read_pickle("GeneratedData/DataFrame.pkl")
predLink = (ranking["IsTestSet"] == 1).sum()
ranking.sort_values("CN", ascending=False, inplace=True)
print('########################################################################')
print('Ranking CN ordered desc \n')
print(ranking.head())

# Values for CN Algorithm #
#Roc Auc CN

fprCN, tprCN, thresholdsCN = sklearn.metrics.roc_curve(ranking.loc[:,"IsTestSet"], ranking.loc[:,"CN"], pos_label=1)
roc_aucCN = sklearn.metrics.auc(fprCN, tprCN)
print("The RocAuc Score for CN is: " + str(roc_aucCN) + '\n')

plt.figure()     
lw = 2
plt.plot(fprCN,tprCN,color="darkorange",lw=lw, label="ROC curve (area = %0.2f)" % roc_aucCN,) 
plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate") 
plt.title("RocAuc CN - DBLP Coauthor network Articles")
plt.legend(loc="lower right")
plt.savefig('rocaucCN DBLP')

#Precision CN

rankingCn = (ranking.iloc[0:lenGset_edges]["IsTestSet"] == 1).sum()
print ("The Precision Score with CN Algorithm is: " + str(rankingCn / lenGset_edges) + '\n')
fpCN, fnCN = lenGset_edges - rankingCn, lenGset_edges - rankingCn
tnCN = (ranking.iloc[lenGset_edges:]["IsTestSet"] == 0).sum()
print('CN -> TruePositive: ',rankingCn, ', FalsePositive: ', fpCN, ' FalseNegative: ', fnCN,' TrueNegative: ', tnCN)


# Values for Jaccard Coefficient Algorithm #

#Roc Auc JA
print('########################################################################\n')
ranking.sort_values("JaccardCoefficient", ascending=False, inplace=True)
print('Ranking JA ordered desc \n')
print(ranking.head())

fprJA, tprJA, thresholdsJA = sklearn.metrics.roc_curve(ranking.loc[:,"IsTestSet"], ranking.loc[:,"JaccardCoefficient"], pos_label=1)
roc_aucJA = sklearn.metrics.auc(fprJA, tprJA)
print("The RocAuc Score for Jaccard Coefficient is: " + str(roc_aucJA) + '\n')

plt.figure()     
lw = 2
plt.plot(fprJA,tprJA,color="darkorange",lw=lw, label="ROC curve (area = %0.2f)" % roc_aucJA,) 
plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate") 
plt.title("RocAuc JA - DBLP Coauthor network Articles")
plt.legend(loc="lower right")
plt.savefig('rocaucJA DBLP')


#Precision JA
rankingJA = (ranking.iloc[0:lenGset_edges]["IsTestSet"] == 1).sum()
print ("The Precision Score with JA Algorithm is: " + str(rankingJA / lenGset_edges) + '\n')
fpJA, fnJA = lenGset_edges - rankingJA, lenGset_edges - rankingJA
tnJA = (ranking.iloc[lenGset_edges:]["IsTestSet"] == 0).sum()

print('JA -> TruePositive: ',rankingJA, ', FalsePositive: ', fpJA, ' FalseNegative: ', fnJA,' TrueNegative: ', tnJA)

print('########################################################################\n')

# Values for AdamicAdar Algorithm #

#Roc Auc AA
ranking.sort_values("AdamicAdar", ascending=False, inplace=True)
print('Ranking AA ordered desc \n')
print(ranking.head())


fprAA, tprAA, thresholdsAA = sklearn.metrics.roc_curve(ranking.loc[:,"IsTestSet"], ranking.loc[:,"AdamicAdar"], pos_label=1)
roc_aucAA = sklearn.metrics.auc(fprAA, tprAA)
print("The RocAuc Score for AdamicAdar is: " + str(roc_aucAA) + '\n')

plt.figure()     
lw = 2
plt.plot(fprAA,tprAA,color="darkorange",lw=lw, label="ROC curve (area = %0.2f)" % roc_aucAA,) 
plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate") 
plt.title("RocAuc AA - DBLP Coauthor network Articles")
plt.legend(loc="lower right")
plt.savefig('rocaucAA DBLP')

rankingAA = (ranking.iloc[0:lenGset_edges]["IsTestSet"] == 1).sum()
print ("The Precision Score with AA Algorithm is: " + str(rankingAA / lenGset_edges) + '\n')

fpAA, fnAA = lenGset_edges - rankingAA, lenGset_edges - rankingAA
tnAA = (ranking.iloc[lenGset_edges:]["IsTestSet"] == 0).sum()

print('AA -> TruePositive: ',rankingAA, ', FalsePositive: ', fpAA, ' FalseNegative: ', fnAA,' TrueNegative: ', tnAA)


plt.figure()     
lw = 2
plt.plot(fprAA,tprAA,color="blue",lw=lw, label="AA" % roc_aucAA,) 
plt.plot(fprJA,tprJA,color="green",lw=lw, label="JA" % roc_aucJA,) 
plt.plot(fprCN,tprCN,color="darkorange",lw=lw, label="CN" % roc_aucCN,) 
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate") 
plt.title("RocAuc Comparison")
plt.legend(loc="lower right")
plt.savefig('rocaucComparison.png')