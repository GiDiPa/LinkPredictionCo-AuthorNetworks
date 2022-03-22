import networkx as nx

import random

G=nx.Graph()
list1 = []
list2 = []

with open('GeneratedData/netscience_nodes') as textfile:
    for line in textfile:
        #print(line.split(' ')[0])
        list1.append(line.split('\n')[0])

print()

for i in list1:    
    G.add_node(i)       

print(len(G.nodes()))

with open('GeneratedData/netscience_edges') as textfile2:
    for line in textfile2:
        list2.append(line.split(','))

for j in list2:
    G.add_edge(j[0].strip('\n'),j[1].strip('\n'))

#print(G.nodes())
#print(G.edges())
G = nx.convert_node_labels_to_integers(G, first_label=0, ordering='default')
nx.write_gml(G, "GeneratedData/NetScienceGraph.gml")

#create a test and training set
random.seed()
test_edge_list_split = random.sample(G.edges(), int(0.2 * G.number_of_edges()))
test_edge_list = list(test_edge_list_split)

# Remove some edges
training_graph = G.copy()
training_graph.remove_edges_from(test_edge_list_split)
training_edge_list = list(training_graph.edges())
test_graph = G.copy()
test_graph.remove_edges_from(training_edge_list)

training_graph = nx.convert_node_labels_to_integers(training_graph, first_label=0, ordering='default')
test_graph = nx.convert_node_labels_to_integers(test_graph, first_label=0, ordering='default')

nx.write_gml(training_graph, "GeneratedData/trainingNetScience.gml")
nx.write_gml(test_graph, "GeneratedData/testNetScience.gml")
