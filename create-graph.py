import networkx as nx
import shapely
import csv
import random

#import an adjacency graph exported from QGIS & create a networkx graph

def read_file(file):
	with open(file, 'r') as f:
		reader = csv.reader(f, delimiter=',')
		reader.next() #skip header
		results = [row for row in reader]

	return results

def build_graph():
	#from the adjacency data, build the graph -- assume each row of CSV is a pair of node IDs which are connected by an edge
	#and population data are contained within the 3rd and 4th fields

	data = read_file('MN-sample-area/mcd2010-graph.csv')
	nodes = set([x[0] for x in data])
	edges = [(x[0],x[2]) for x in data if x[2]!='']

	G = nx.Graph()

	G.add_nodes_from(nodes)
	G.add_edges_from(edges)

	#link the population data as weights

	weights = [(x[3],x[9]) for x in read_file('MN-sample-area/weights.csv')]

	for weight in weights:
		G.nodes[weight[0]]['weight']=weight[1]

	return G

if __name__ == "__main__":
	G = build_graph()