import networkx as nx
import Graph_Sampling
import random

path_file = '/home/dplz/PythonProject/LinkPrediction DBLP/LinkPrediction/DatasetTrainTest/GeneratedData/co-authorNetwork.gml'
G = nx.read_gml(path_file) 

test_edge_list_split = random.sample(G.edges(), int(0.2 * G.number_of_edges()))
test_edge_list = list(test_edge_list_split)

# Remove some edges
training_graph = G.copy()
training_graph.remove_edges_from(test_edge_list_split)
training_edge_list = list(training_graph.edges())
test_graph = G.copy()
test_graph.remove_edges_from(training_edge_list)

m = test_graph.number_of_edges()
m1 = training_graph.number_of_edges()
m2 = G.number_of_edges()

#test_edge_list = list(test_graph.edges(data=True))
textfile = open("GeneratedData/testlist.txt", "w")
for element in test_edge_list:
    textfile.write(str(element) + '\n')
textfile.close()
nx.write_gml(training_graph, "GeneratedData/training.gml")
nx.write_gml(test_graph, "GeneratedData/test.gml")

'''
test_edge_list = list(test_graph.edges(data=True))
textfile = open("GeneratedData/testlistsmall.txt", "w")
for element in test_edge_list:
    textfile.write(str(element) + '\n')
textfile.close()
nx.write_gml(training_graph, "GeneratedData/trainingsmall.gml")
'''

print("Number of edges test :", str(m))
print("Number of edges training:", str(m1))
print("Number of edges G:", str(m2))

print("Number of connected components test :", str(nx.number_connected_components(test_graph)))
print("Number of connected components training :", str(nx.number_connected_components(training_graph)))
print("Number of connected components G :", str(nx.number_connected_components(G)))

