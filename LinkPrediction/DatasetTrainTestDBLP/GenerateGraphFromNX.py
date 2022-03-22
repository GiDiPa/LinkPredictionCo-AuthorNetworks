import csv
import networkx as nx
from itertools import combinations
import ast

# costruzione semplice del grafo: accede al file csv e prende i nomi dalla lista nella seconda colonna di ogni riga
# creando tutte le combinazioni possibili a coppia. 
g = nx.Graph()
default_weight = 1
for row in csv.reader(open(r"../CreatingCSVProcess/OutputData/co-authorNetwork.csv", 'r', encoding='utf8')):
    if '[' in row[2]:
        lista = row[2]
        #trasformazione da stringa a lista
        lista = ast.literal_eval(lista)
        edges = combinations(lista, 2)
        #aggiunta dei nodi della lista (autori)
        g.add_nodes_from(lista)
        #aggiunta degli archi pesati con le combinazioni create
        for edge in edges:
            if edge in g.edges():
                g[edge[0]][edge[1]]['weight'] += default_weight
                #edges.remove(edge)
            else:
                g.add_edge(edge[0],edge[1])
                g[edge[0]][edge[1]]['weight'] = default_weight
                
print(len(list(g.nodes())))

#g.remove_nodes_from(list(nx.isolates(g)))                

for component in list(nx.connected_components(g)):
    if len(component)<3:
        for node in component:
            g.remove_node(node)

#esporto il grafo in formato gexf per lo studio dello stesso
nx.write_gml(g, "GeneratedData/co-authorNetwork.gml")

print(len(list(g.nodes())))

