import multiprocessing
import networkx as nx
import pickle
import tqdm
import os
import math

G = pickle.load(open('GeneratedData/GTrainingIndexedWithLabel.pkl', 'rb'))
#G = nx.convert_node_labels_to_integers(G, first_label=0, ordering='default', label_attribute = 'name_label')


if not(os.path.isfile("GeneratedData/mp_cn_alg_resultsDefinitive2.txt")):
  textfile = open("GeneratedData/mp_cn_alg_resultsDefinitive2.txt", "a")
  textfile.write('| Node1 | Node2 | CNCard | JaccardC | AdamicA |\n') 
  textfile.close()
  input('if')
  textfile = open("GeneratedData/mp_cn_alg_resultsDefinitive2.txt", "a")
  Glist_nodes_ext = list(G.nodes())
  Glist_nodes_ext_copy = Glist_nodes_ext.copy()
  Glist_nodes_int = list(G.nodes())
  Gset_edges = set(G.edges())
else:
  input('else')
  textfile = open("GeneratedData/mp_cn_alg_resultsDefinitive2.txt", "a")
  Glist_nodes_ext = pickle.load(open('GeneratedData/BackupExt.pkl', 'rb'))
  Glist_nodes_ext_copy = Glist_nodes_ext.copy()
  Glist_nodes_int = list(G.nodes())
  Gset_edges = set(G.edges())



def linkPredProcessSimplified(node_ext):
  internalCheckpoint = True
  for node_int in Glist_nodes_int:
    if node_int != node_ext and internalCheckpoint:
      continue
    else:
      if node_int == node_ext:
        internalCheckpoint = False
      else:
        if tuple((node_ext, node_int)) not in Gset_edges:
          nbor_i = set([n for n in G.neighbors(node_ext)])
          nbor_j = set([n for n in G.neighbors(node_int)])
          if nbor_i.intersection(nbor_j):
            aa = 0
            jac = len(nbor_i.intersection(nbor_j)) / float(len(nbor_i | nbor_j))
            for w in nbor_i.intersection(nbor_j):
              aa = aa + 1 / math.log(G.degree(w))  
          else:
            aa = 0
            cn = 0
            jac = 0
          textfile.write(str(node_ext) + ',' + str(node_int) + ',' + str(len(nbor_i.intersection(nbor_j))) + ',' + str(jac) + ',' + str(aa) + '\n')

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


