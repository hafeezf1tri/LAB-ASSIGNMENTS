import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import heapq

# The 10 locations in Perak with costs
perak_graph = {
    'Ipoh': {'Taiping': 10, 'Kuala Kangsar': 20, 'Batu Gajah': 30, 'Kampar': 40},
    'Taiping': {'Ipoh': 10, 'Kuala Kangsar': 25, 'Teluk Intan': 35},
    'Kuala Kangsar': {'Ipoh': 20, 'Taiping': 25, 'Gerik': 30},
    'Teluk Intan': {'Taiping': 35, 'Batu Gajah': 20, 'Manjung': 15},
    'Batu Gajah': {'Ipoh': 30, 'Teluk Intan': 20, 'Kampar': 10},
    'Kampar': {'Ipoh': 40, 'Batu Gajah': 10, 'Tanjung Malim': 25},
    'Manjung': {'Teluk Intan': 15, 'Tanjung Malim': 40},
    'Tanjung Malim': {'Kampar': 25, 'Manjung': 40, 'Slim River': 10},
    'Slim River': {'Tanjung Malim': 10, 'Gerik': 50},
    'Gerik': {'Kuala Kangsar': 30, 'Slim River': 50}
}

# Function to visualize the graph
def visualize_graph(graph):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, cost in neighbors.items():
            G.add_edge(node, neighbor, weight=cost)
    pos = graphviz_layout(G, prog='dot')
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=15, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title('Graph Structure: 10 Locations in Perak with Costs')
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

# uniform Cost Search (UCS) function
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
            for neighbor, edge_cost in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, neighbor, path))
    return []

# user input for start location and goal, all algorithms are used in a while loop
def main():
    visualize_graph(perak_graph)
    print("INPUT IS CASE SENSITIVE, BE WARY")

    while True:
        start_location = input("Enter the start location (or type 'exit' to quit): ")
        if start_location.lower() == 'exit':
            break

        destination = input("Enter the destination: ")
        if destination.lower() == 'exit':
            break

        if start_location not in perak_graph or destination not in perak_graph:
            print("Invalid locations. Please enter valid start and destination locations from the graph.")
            continue

        # Run BFS
        bfs_path = bfs(perak_graph, start_location, destination)
        if bfs_path:
            print(f"Path from {start_location} to {destination} using BFS: {bfs_path}")
        else:
            print(f"No path found from {start_location} to {destination} using BFS.")

        # Run DFS
        dfs_path = dfs(perak_graph, start_location, destination)
        if dfs_path:
            print(f"Path from {start_location} to {destination} using DFS: {dfs_path}")
        else:
            print(f"No path found from {start_location} to {destination} using DFS.")

        # Run UCS
        ucs_path = ucs(perak_graph, start_location, destination)
        if ucs_path:
            print(f"Path from {start_location} to {destination} using UCS: {ucs_path}")
        else:
            print(f"No path found from {start_location} to {destination} using UCS.")

if __name__ == "__main__":
    main()