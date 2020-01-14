import os
import networkx as nx

from core.langdict import LangDict
from core.to_acyclic import to_acyclic
#combine all csvs into one graph
directory = '/Users/peterwalker/Desktop/projects/langdict/core/data/Dictionary_in_csv/'

#build new graph from the separate csvs
G = LangDict()

for file in os.listdir(directory):
        temp = LangDict.from_csv(directory + file)
        G = G.add(temp)


'''#build new graph from the combined csvs

g = nx.DiGraph()
nx.from_dict_of_lists(LangDict.from_csv(file), create_using=g)
g = g.reverse()'''

#pickle here? probs
#g = to_acyclic(g)
