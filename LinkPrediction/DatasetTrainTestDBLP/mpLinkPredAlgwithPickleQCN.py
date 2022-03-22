import multiprocessing
import time
from multiprocessing import Pool
from unicodedata import name
import networkx as nx
import pickle
import tqdm
import os
import math


G = pickle.load(open('GeneratedData/GTrainingIndexedWithLabel.pkl', 'rb'))
#G = nx.convert_node_labels_to_integers(G, first_label=0, ordering='default', label_attribute = 'name_label')


if not(os.path.isfile("GeneratedData/mp_qcn_alg_results.txt")):
  textfile = open("GeneratedData/mp_qcn_alg_results.txt", "a")
  textfile.write('| Node1 | Node2 | JaccardQCN | AdamicAQCN |\n')
  textfile.close() 
  input('if')
  Glist_nodes_ext = list(G.nodes())
  Glist_nodes_ext_copy = Glist_nodes_ext.copy()
  Glist_nodes_int = list(G.nodes())
  Gset_edges = set(G.edges())
  textfile = open("GeneratedData/mp_qcn_alg_results.txt", "a")
else:
  input('else')
  textfile = open("GeneratedData/mp_qcn_alg_results.txt", "a")
  Glist_nodes_ext = pickle.load(open('GeneratedData/BackupExt.pkl', 'rb'))
  Glist_nodes_ext_copy = Glist_nodes_ext.copy()
  Glist_nodes_int = list(G.nodes())
  Gset_edges = set(G.edges())



def linkPredProcessSimplified(node_ext):
  internalCheckpoint = True
  nbor_i = set([n for n in G.neighbors(node_ext)])
  for node_int in Glist_nodes_int:
    if node_int != node_ext and internalCheckpoint:
      continue
    else:
      if node_int == node_ext:
        internalCheckpoint = False
      else:
        if tuple((node_ext, node_int)) not in Gset_edges:
          qcn = set()
          nbor_j = set([n for n in G.neighbors(node_int)])
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
                aa_f = aa_f + ((1 / math.log(G.degree(w))) + (1/(len(nbor_i) + len(nbor_j))))
            for z in qcn:
                aa_s = aa_s + (1 / math.log(G.degree(z)))

            aaQCN = float(aa_f * aa_s)

            textfile.write(str(node_ext) + ',' + str(node_int) + ',' + str("%.8f" % jacQCN) + ',' + str("%.8f" % aaQCN) + '\n')
  return node_ext
  

  
pool = multiprocessing.Pool()
a = 0
for result in tqdm.tqdm(pool.imap(linkPredProcessSimplified, Glist_nodes_ext), total=len(Glist_nodes_ext)):
  a += 1
  Glist_nodes_ext_copy.remove(result)
  if a % 10000 == 0:
    pickle.dump(Glist_nodes_ext_copy, open('GeneratedData/BackupExt.pkl', 'wb'))

pickle.dump(Glist_nodes_ext_copy, open('GeneratedData/BackupExt.pkl', 'wb'))
textfile.close()

