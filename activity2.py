import networkx as nx
import matplotlib.pyplot as plt

# Define the graph using sets for the adjacency list
graph_03 = {
    'S': set(['A', 'B', 'C']),
    'A': set(['D', 'E', 'S']),
    'D': set(['A']),
    'E': set(['A']),
    'B': set(['F', 'S']),
    'F': set(['B']),
    'C': set(['H', 'I', 'S']),
    'H': set(['C']),
    'I': set(['J', 'K', 'C']),
    'J': set(['G', 'L']),
    'G': set(['J']),
    'L': set(['J']),
    'K': set(['I'])
}

# Create a graph
G = nx.Graph()

# Add nodes and edges from the adjacency list
for node, neighbors in graph_03.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Define the positions of each node manually if a specific layout is desired
pos = nx.spring_layout(G)

# Draw the graph with specified positions
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=15, font_weight='bold', arrows=True, arrowstyle='->', arrowsize=20)
plt.title('Graph Structure Using Sets (graph_03)')
plt.show()