import networkx as nx
import matplotlib.pyplot as plt

from ..langdict import LangDict
from ..to_acyclic import to_acyclic

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

#before graph
nx.draw_networkx(g, arrows=True)
plt.draw()
plt.show()

#calling the function to be tested
G = to_acyclic(g)

# Display the info
nx.draw_networkx(G, arrows=True)
plt.draw()
plt.show()
