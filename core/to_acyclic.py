import networkx as nx

# create new graph with contracted cycles, that also preserves node
# information. the result is transforming a cyclic to an acyclic graph

def to_acyclic(g):
    counter = 0
    while True:
        try:
            # 1. identify a cycle
            combined_nodes = nx.find_cycle(g)[0] #tuple
            preserved_node = combined_nodes[0] #string first, becomes tuple
            deleted_node = combined_nodes[1] #string first, becomes tuple

            '''if type(deleted_node) != str:
                print(deleted_node)'''

            # 2. Contract the first two nodes of the cycle
            g = nx.contracted_nodes(g,
                preserved_node, deleted_node,
                self_loops=False
                )

            # 3. Relabel the nodes so that information in the the deleted node
            # is not lost.
            # Check for self by checking if two nodes to be collapsed
            # share any values

            # need the union of the two previous two nodes to be the new
            # node instead of if __ not in __
            g = nx.relabel.relabel_nodes(g, {preserved_node:
                frozenset(preserved_node) | frozenset(deleted_node)
            } )

        except nx.exception.NetworkXNoCycle:
            break

        counter +=1
        print("{} nodes collapsed\r".format(counter))
    return g

#________________________________LOG_____________________________________
# right now this only creates a graph and doesnt preserve
# directional data, so instead of using from_dict_of_lists,
# mimic its behavior from the source code by using
# add_edges_from possibly

    #SOLVED
    #create_using works in this` case if a digraph is initialized
    #separately

# need to combine find cycle and contracted nodes in a way that
# preserves node info, possibly use a temp tuple

    #SOLVED
    #1. nx.find_cycle[0] = temp tuple
    #2. contracted_nodes
    #3. nx.relabel.relabel_nodes

#need to combine tuples in a non nesting way
    #SOLVED by forcing tuple concatination

#investigate doubles, d is a self looping node
    #SOLVED by if deleted_node not in preserved_node
