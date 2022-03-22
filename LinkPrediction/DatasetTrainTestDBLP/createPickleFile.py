import networkx as nx
import pickle
''''''
path_file = '/home/dplz/PythonProject/LinkPrediction DBLP/LinkPrediction/DatasetTrainTest/GeneratedData/training.gml'

G = nx.read_gml(path_file)

pickle.dump(G, open('GeneratedData/GTraining.pkl', 'wb'))

path_file = '/home/dplz/PythonProject/LinkPrediction DBLP/LinkPrediction/DatasetTrainTest/GeneratedData/test.gml'

G = nx.read_gml(path_file)

pickle.dump(G, open('GeneratedData/GTest.pkl', 'wb'))



#G = pickle.load(open('GeneratedData/GTraining.pkl', 'rb'))
#G = nx.convert_node_labels_to_integers(G, first_label=0, ordering='default', label_attribute = 'name_label')
#pickle.dump(G, open('GeneratedData/GTrainingIndexedWithLabel.pkl', 'wb'))

#G = pickle.load(open('GeneratedData/GTest.pkl', 'rb'))
#G = nx.convert_node_labels_to_integers(G, first_label=0, ordering='default', label_attribute = 'name_label')
#pickle.dump(G, open('GeneratedData/GTestIndexedWithLabel.pkl', 'wb'))