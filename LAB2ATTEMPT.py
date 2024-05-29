import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import heapq

# The 10 locations in Perak
perak_graph = {
    'Ipoh': {'Taiping', 'Kuala Kangsar', 'Batu Gajah', 'Kampar'},
    'Taiping': {'Ipoh', 'Kuala Kangsar', 'Teluk Intan'},
    'Kuala Kangsar': {'Ipoh', 'Taiping', 'Gerik'},
    'Teluk Intan': {'Taiping', 'Batu Gajah', 'Manjung'},
    'Batu Gajah': {'Ipoh', 'Teluk Intan', 'Kampar'},
    'Kampar': {'Ipoh', 'Batu Gajah', 'Tanjung Malim'},
    'Manjung': {'Teluk Intan', 'Tanjung Malim'},
    'Tanjung Malim': {'Kampar', 'Manjung', 'Slim River'},
    'Slim River': {'Tanjung Malim', 'Gerik'},
    'Gerik': {'Kuala Kangsar', 'Slim River'}
}

# Function to visualize the graph
def visualize_graph(graph):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    pos = graphviz_layout(G, prog='dot')
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=15, font_weight='bold')
    plt.title('Graph Structure: 10 Locations in Perak')
    plt.show(block=False)

# Breadth-First Search (BFS) function
def bfs(graph, start, goal):
    visited = []
    queue = [start]
    while queue:
        print("Visited:", visited)
        print("Queue:", queue)
        current = queue.pop(0)
        if current not in visited:
            visited.append(current)
            if current == goal:
                break
            for neighbor in graph[current]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited

# Depth-First Search (DFS) function
def dfs(graph, start, goal):
    visited = []
    stack = [start]
    while stack:
        current = stack.pop()
        print("Current node is:", current)
        if current == goal:
            visited.append(current)
            break
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
        visited.append(current)
        print("Visited is:", visited)
    return visited

# Uniform Cost Search (UCS) function
def ucs(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]  # (cost, node, path)
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == goal:
                return path
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + 1, neighbor, path))
    return []

# User input for start location, goal, and the algorithm
def main():
    visualize_graph(perak_graph)
    print("INPUT IS CASE SENSITIVE, BE WARY")
    start_location = input("Enter the start location: ")
    destination = input("Enter the destination: ")

    if start_location not in perak_graph or destination not in perak_graph:
        print("Invalid locations. Please enter valid start and destination locations from the graph.")
        return

    algorithm = input("Enter the algorithm (BFS, DFS, UCS): ").strip().upper()

    if algorithm == "BFS":
        path = bfs(perak_graph, start_location, destination)
    elif algorithm == "DFS":
        path = dfs(perak_graph, start_location, destination)
    elif algorithm == "UCS":
        path = ucs(perak_graph, start_location, destination)
    else:
        print("Invalid algorithm choice. Please enter BFS, DFS, or UCS.")
        return

    if path:
        print(f"Path from {start_location} to {destination} using {algorithm}: {path}")
    else:
        print(f"No path found from {start_location} to {destination} using {algorithm}.")

if __name__ == "__main__":
    main()