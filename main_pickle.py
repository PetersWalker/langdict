import os
import networkx as nx
import matplotlib.pyplot as plt
import pickle

from core.langdict import LangDict

#combine all csvs into one graph
directory = '/Users/peterwalker/Desktop/projects/langdict/core/data/Dictionary_in_csv/'

#build new graph from the separate csvs
dict = LangDict()

#each file turns into a Langdict object, then gets added together into one
for file in os.listdir(directory):
        temp = LangDict.from_csv(directory + file)
        dict = dict.add(temp)

#turn the dictionary into a Digraph for analysis
g = nx.DiGraph()
nx.from_dict_of_lists(dict, create_using=g)
g = g.reverse()

#determine the stronly connected components
scc = nx.strongly_connected_components(g)

#size of each dictionary
digraph_count = len(dict)
scc_count = sum(1 for comp in scc)

print('there are {} strongly connected components out of {} definitions'.format(scc_count, digraph_count))
G = nx.condensation(g, scc=scc)
print(len(G))

with open("G.pickle", "wb") as pickle_file:
    pickle.dump(G, pickle_file)
