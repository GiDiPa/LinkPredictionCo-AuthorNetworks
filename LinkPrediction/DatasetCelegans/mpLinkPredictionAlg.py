from asyncore import read
import networkx as nx
import os
import math

G = nx.read_gml('GeneratedData/trainingCelegans.gml')

if not(os.path.isfile("GeneratedData/mp_lp_alg_resultsDefinitive.txt")):
  textfile = open("GeneratedData/mp_lp_alg_resultsDefinitive.txt", "w")
  textfile.write('| Node1 | Node2 | CNCard | JaccardC | PrefAttach | AdamicA | QCNJA | QCNAA |\n')
  textfile.close() 
  input('if')
  textfile = open("GeneratedData/mp_lp_alg_resultsDefinitive.txt", "a")
  Gset_edges = set(G.edges())
else:
  input('else')
  textfile = open("GeneratedData/mp_lp_alg_resultsDefinitive.txt", "a")
  Gset_edges = set(G.edges())

  
  
#nonedges = list(nx.non_edges(G))
#print(len(nonedges))
#a = 0
nodesList = list(G.nodes())

for i in nodesList:
  internalCheckpoint = True
  for j in nodesList:
    if i != j and internalCheckpoint:
      continue
    else:
      if i == j:
        internalCheckpoint = False
      else:
        if tuple((i,j)) not in Gset_edges:
          nbor_i = set([n for n in G.neighbors(i)])
          nbor_j = set([n for n in G.neighbors(j)])
          prefAtt = G.degree(i) * G.degree(j)
          if nbor_i.intersection(nbor_j):
            aa = 0
            jac = len(nbor_i.intersection(nbor_j)) / float(len(nbor_i | nbor_j))
            for w in nbor_i.intersection(nbor_j):
              aa = aa + 1 / math.log(G.degree(w))
              cn = len(nbor_i.intersection(nbor_j))
          else:
            aa = 0
            jac = 0
            cn = 0
          qcn = set()
          for nnbor in nbor_i:
            for nnbor2 in nbor_j:
              if tuple((nnbor, nnbor2)) in Gset_edges:
                qcn.add(nnbor)
                qcn.add(nnbor2)
          if len(qcn):
            jacQCN = float(len(nbor_i.intersection(nbor_j)) / len(nbor_i.union(nbor_j))) + ((1/(len(nbor_i) + len(nbor_j))) * (len(qcn)/len(nbor_i.union(nbor_j))))
            aa_f = 0
            aa_s = 0
            for w in nbor_i.intersection(nbor_j):
              aa_f = aa_f + ((1 / math.log(G.degree(w))))
            for z in qcn:
              aa_s = aa_s + (1/(len(nbor_i) + len(nbor_j))) * (1 / math.log(G.degree(z)))
            aaQCN = float(aa_f + aa_s)
          else:
            jacQCN = jac
            aaQCN = aa
          
          textfile.write(str(i) + ',' + str(j) + ',' + str(cn) + ',' + str(jac) + ',' + str(prefAtt) + ',' + str(aa) + ',' + str(jacQCN) + ',' + str(aaQCN) + '\n')

textfile.close()



  
