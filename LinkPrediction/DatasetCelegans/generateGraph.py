import networkx as nx
import random 

G=nx.Graph()

list1 = []
list2 = []

with open('GeneratedData/C-Elegans_nodes') as textfile:
    for line in textfile:
        #print(line.split(' ')[0])
        list1.append(line.split('\n')[0])

for i in list1:    
    G.add_node(i)       

with open('GeneratedData/C-Elegans_edges') as textfile2:
    for line in textfile2:
        list2.append(line.split(','))

for j in list2:
    G.add_edge(j[0].strip('\n'),j[1].strip('\n'))

G = nx.convert_node_labels_to_integers(G, first_label=0, ordering='default')
nx.write_gml(G, "GeneratedData/CElegansGraph.gml")

#split in training and test 
random.seed()
test_edge_list_split = random.sample(G.edges(), int(0.2 * G.number_of_edges()))
test_edge_list = list(test_edge_list_split)

# Remove some edges
training_graph = G.copy()
training_graph.remove_edges_from(test_edge_list_split)
training_edge_list = list(training_graph.edges())
test_graph = G.copy()
test_graph.remove_edges_from(training_edge_list)

#test_edge_list = list(test_graph.edges(data=True))

training_graph = nx.convert_node_labels_to_integers(training_graph, first_label=0, ordering='default')
test_graph = nx.convert_node_labels_to_integers(test_graph, first_label=0, ordering='default')

nx.write_gml(training_graph, "GeneratedData/trainingCelegans.gml")
nx.write_gml(test_graph, "GeneratedData/testCelegans.gml")