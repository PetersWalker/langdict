import networkx as nx
import matplotlib.pyplot as plt

from ..langdict import LangDict

letters = {'a':['c','e','g'],
        'b':['a','d','c','e','f','g',],
        'c':['a','d','g','h'],
        'd':['d','c','f','g'],
        'e':['d','g'],
        'f':['j'],
        'g':['h'],
        'h':['a','e','g'],
        'i':[],
        'j':['a','g'],
        'k':['e','f','g']
        }

# the digraph datastructure from LangDict object
g = nx.DiGraph()
nx.from_dict_of_lists(LangDict(letters), create_using=g)
g = g.reverse()

it = nx.strongly_connected_components(g)

for item in it:
    print(item)
