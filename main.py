import pickle
import networkx

with open("G.pickle", "rb") as pickle_file:
    g = pickle.load(pickle_file)

order = g.order()

print(order)

print(g.graph)
