import os
import networkx as nx

from core.langdict import LangDict
from core.to_acyclic import to_acyclic
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

#pickle here? probs
g = to_acyclic(g)
