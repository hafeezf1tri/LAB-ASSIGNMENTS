import networkx as nx
import matplotlib.pyplot as plt
import graphviz

# Define the adjacency list for the graph
graph_01 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['E']
}

# Create a graph
G = nx.Graph()

# adding edges for graph
for node, neighbors in graph_01.items():
    for neighbor in neighbors:
        G.add_edge(node,neighbor)


pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='dot')

# drawing the graph
nx.draw(G, with_labels=True, arrows=True, arrowstyle='->', arrowsize=20)
plt.show()