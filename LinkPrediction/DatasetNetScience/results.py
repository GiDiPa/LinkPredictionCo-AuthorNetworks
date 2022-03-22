import numpy as np
import pandas as pd
import sklearn.metrics
import pickle
import matplotlib.pyplot as plt
import networkx as nx
import math
import gc

print('NetScience Results')
G = nx.read_gml('GeneratedData/testNetScience.gml')
lenGset_edges = len(set(G.edges()))
print('The number of links in Test Set is: ', lenGset_edges, ' \n')


#pd.DataFrame(cnList,columns=['Node1', 
                      #'Node2', 'CN', 'JaccardCoefficient', 'AdamicAdar','QCNJacCoeff', 'QCNAdamicA', 'IsTestSet'])

ranking = pd.read_pickle("GeneratedData/DataFrameNetScience.pkl")

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
plt.title("CN RocAuc")
plt.legend(loc="lower right")
plt.savefig('GeneratedData/plots/rocaucCN.png')


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
plt.plot(fprJA,tprJA,color="green",lw=lw, label="ROC curve (area = %0.2f)" % roc_aucJA,) 
plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate") 
plt.title("Jaccard Coefficient RocAuc")
plt.legend(loc="lower right")
plt.savefig('GeneratedData/plots/rocaucJA.png')


#Precision JA

rankingJA = (ranking.iloc[0:lenGset_edges]["IsTestSet"] == 1).sum()
print ("The Precision Score with JA Algorithm is: " + str(rankingJA / lenGset_edges) + '\n')

fpJA, fnJA = lenGset_edges - rankingJA, lenGset_edges - rankingJA
tnJA = (ranking.iloc[lenGset_edges:]["IsTestSet"] == 0).sum()

print('JA -> TruePositive: ',rankingJA, ', FalsePositive: ', fpJA, ' FalseNegative: ', fnJA,' TrueNegative: ', tnJA)

print('########################################################################\n')
# Values for PrefAttachment #

#Roc Auc PA
ranking.sort_values("PrefAttachment", ascending=False, inplace=True)
print('Ranking PA ordered desc \n')
print(ranking.head())

fprPA, tprPA, thresholdsPA = sklearn.metrics.roc_curve(ranking.loc[:,"IsTestSet"], ranking.loc[:,"PrefAttachment"], pos_label=1)
roc_aucPA = sklearn.metrics.auc(fprPA, tprPA)
print("The RocAuc Score for PrefAttachment is: " + str(roc_aucPA) + '\n')

plt.figure()     
lw = 2
plt.plot(fprPA,tprPA,color="pink",lw=lw, label="ROC curve (area = %0.2f)" % roc_aucPA,) 
plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate") 
plt.title("Pref Attachment RocAuc")
plt.legend(loc="lower right")
plt.savefig('GeneratedData/plots/rocaucPA.png')


#Precision PrefAttachment

rankingPA = (ranking.iloc[0:lenGset_edges]["IsTestSet"] == 1).sum()
print ("The Precision Score with PA Algorithm is: " + str(rankingPA / lenGset_edges) + '\n')


fpPA, fnPA = lenGset_edges - rankingPA, lenGset_edges - rankingPA
tnPA = (ranking.iloc[lenGset_edges:]["IsTestSet"] == 0).sum()

print('PA -> TruePositive: ',rankingPA, ', FalsePositive: ', fpPA, ' FalseNegative: ', fnPA,' TrueNegative: ', tnPA)

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
plt.plot(fprAA,tprAA,color="blue",lw=lw, label="ROC curve (area = %0.2f)" % roc_aucAA,) 
plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate") 
plt.title("CN RocAuc")
plt.legend(loc="lower right")
plt.savefig('GeneratedData/plots/rocaucAA.png')

#Precision AA

rankingAA = (ranking.iloc[0:lenGset_edges]["IsTestSet"] == 1).sum()
print ("The Precision Score with AA Algorithm is: " + str(rankingAA / lenGset_edges) + '\n')

fpAA, fnAA = lenGset_edges - rankingAA, lenGset_edges - rankingAA
tnAA = (ranking.iloc[lenGset_edges:]["IsTestSet"] == 0).sum()

print('AA -> TruePositive: ',rankingAA, ', FalsePositive: ', fpAA, ' FalseNegative: ', fnAA,' TrueNegative: ', tnAA)


print('########################################################################\n')
# Values for QCN JAccard Coefficient Algorithm #

#Roc Auc QCNJa
ranking.sort_values("QCNJacCoeff", ascending=False, inplace=True)
print('Ranking QCNJA ordered desc \n')
print(ranking.head())

fprQCNJA, tprQCNJA, thresholdsQCNJA = sklearn.metrics.roc_curve(ranking.loc[:,"IsTestSet"], ranking.loc[:,"QCNJacCoeff"], pos_label=1)
roc_aucQCNJA = sklearn.metrics.auc(fprQCNJA, tprQCNJA)
print("The RocAuc Score for QCNJA is: " + str(roc_aucQCNJA) + '\n')

plt.figure()     
lw = 2
plt.plot(fprQCNJA,tprQCNJA,color="yellow",lw=lw, label="ROC curve (area = %0.2f)" % roc_aucQCNJA,) 
plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate") 
plt.title("CN RocAuc")
plt.legend(loc="lower right")
plt.savefig('GeneratedData/plots/rocaucQCNJA.png')

#Precision QCNJa

rankingQCNJA = (ranking.iloc[0:lenGset_edges]["IsTestSet"] == 1).sum()
print ("The Precision Score with QCNJa Algorithm is: " + str(rankingQCNJA / lenGset_edges) + '\n')

fpQCNJA, fnQCNJA = lenGset_edges - rankingQCNJA, lenGset_edges - rankingQCNJA
tnQCNJA = (ranking.iloc[lenGset_edges:]["IsTestSet"] == 0).sum()

print('QCNJA -> TruePositive: ',rankingQCNJA, ', FalsePositive: ', fpQCNJA, ' FalseNegative: ', fnQCNJA,' TrueNegative: ', tnQCNJA)

print('########################################################################\n')

# Values for QCNAdamicAdar Algorithm #


#Roc Auc QCNAA
ranking.sort_values("QCNAdamicA", ascending=False, inplace=True)
print('Ranking QCNAA ordered desc \n')
print(ranking.head())

fprQCNAA, tprQCNAA, thresholdsQCNAA = sklearn.metrics.roc_curve(ranking.loc[:,"IsTestSet"], ranking.loc[:,"QCNAdamicA"], pos_label=1)
roc_aucQCNAA = sklearn.metrics.auc(fprQCNAA, tprQCNAA)
print("The RocAuc Score for QCNAA is: " + str(roc_aucQCNAA) + '\n')

plt.figure()     
lw = 2
plt.plot(fprQCNAA,tprQCNAA,color="red",lw=lw, label="ROC curve (area = %0.2f)" % roc_aucQCNAA,) 
plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate") 
plt.title("CN RocAuc")
plt.legend(loc="lower right")
plt.savefig('GeneratedData/plots/rocaucQCNAA.png')

#Precision QCNAA

rankingQCNAA = (ranking.iloc[0:lenGset_edges]["IsTestSet"] == 1).sum()
print ("The Precision Score with QCNAA Algorithm is: " + str(rankingQCNAA / lenGset_edges) + '\n')


fpQCNAA, fnQCNAA = lenGset_edges - rankingQCNAA, lenGset_edges - rankingQCNAA
tnQCNAA = (ranking.iloc[lenGset_edges:]["IsTestSet"] == 0).sum()

print('QCNAA -> TruePositive: ',rankingQCNAA, ', FalsePositive: ', fpQCNAA, ' FalseNegative: ', fnQCNAA,' TrueNegative: ', tnQCNAA)


#grouping all the stats in one plot

plt.figure()     
lw = 2
plt.plot(fprQCNAA,tprQCNAA,color="red",lw=lw, label="QCNAA" % roc_aucQCNAA,)
plt.plot(fprQCNJA,tprQCNJA,color="yellow",lw=lw, label="QCNJA" % roc_aucQCNJA,) 
plt.plot(fprAA,tprAA,color="blue",lw=lw, label="AA" % roc_aucAA,) 
plt.plot(fprPA,tprPA,color="pink",lw=lw, label="PA" % roc_aucPA,) 
plt.plot(fprJA,tprJA,color="green",lw=lw, label="JA" % roc_aucJA,) 
plt.plot(fprCN,tprCN,color="darkorange",lw=lw, label="CN" % roc_aucCN,) 
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate") 
plt.title("RocAuc Comparison")
plt.legend(loc="lower right")
plt.savefig('GeneratedData/plots/rocaucComparison.png')

