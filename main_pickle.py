import os
import networkx as nx
import matplotlib.pyplot as plt
import pickle

from core.langdict import LangDict

#combine all csvs into one graph
directory = '/Users/peterwalker/Desktop/projects/langdict/core/data/Dictionary_in_csv/'

#build new graph from the separate csvs
dict = LangDict()

#each file to Langdict, add together
for file in os.listdir(directory):
        temp = LangDict.from_csv(directory + file)
        dict = dict.add(temp)

g = nx.DiGraph()
nx.from_dict_of_lists(dict, create_using=g)
g = g.reverse()

scc = nx.strongly_connected_components(g)
count = 0

for i in scc:
    count += 1

print(count)
G = nx.condensation(g, scc=scc)
print(len(G))

with open("G.pickle", "wb") as pickle_file:
    pickle.dump(G, pickle_file)
