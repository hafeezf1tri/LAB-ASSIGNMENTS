import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout #this was a pain to install on a local machine but i dont like colab,
from collections import deque #if u want me to stack stuff im using this..


# the 10 locations, i did not sort them based on distance, i just googled 10 locations in perak
#yes i didnt put seri iskandar im lazy
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

# function to visualise the graph
def visualize_graph(graph):
    # create the garph
    G = nx.Graph()

    # add nodes & edges
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # force the layout of the graph visual into a tree
    pos = graphviz_layout(G, prog='dot')

    # draw the graph with spec
    plt.figure(figsize=(10, 8)) #i wanted to do arrow but it wouldnt make sense for them to not be able to return, so i removed arrow
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=15, font_weight='bold') #parameters of visualisation
    plt.title('graph structure, 10 locations in perak')
    plt.show(block=False) 
    #this keeps the graph window open, at first i used plt.show without block


# Breadth first search functionality
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (vertex, path) = queue.popleft()
        visited.add(vertex)
        print(f"Current node is: {vertex}")
        print(f"Visited is: {list(visited)}")
        
        for neighbor in graph[vertex]:
            if neighbor == goal:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None

# Depth first search functionality
def dfs(graph, start, goal):
    visited = []
    stack = [start]
    
    while stack:
        current = stack.pop()
        print("Current node is: {}".format(current))
        
        if current == goal:
            visited.append(current)
            break
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
        
        visited.append(current)
        print("Visited is: {}".format(visited))
    
    return visited


#user input for start location,

def main():
    visualize_graph(perak_graph)
    #CASE SENSITIVE INPUT
    print(f"INPUT IS CASE SENSITIVE, BE WARY")
    start_location = input("Enter the start location: ")
    destination = input("Enter the destination: ")
    
    if start_location not in perak_graph or destination not in perak_graph:
        print("Invalid locations. Please enter valid start and destination locations from the graph.")
        return
    
    algorithm = input("Enter the algorithm (BFS or DFS): ").strip().upper()
    
    if algorithm == "BFS":
        path = bfs(perak_graph, start_location, destination) #shoves the input in bfs
    elif algorithm == "DFS":
        path = dfs(perak_graph, start_location, destination) #shoves the input in dfs
    else:
        print("Invalid algorithm choice. Please enter BFS or DFS.")
        return
    
    #exception checking if input is correct, honestly i didnt wanna do this tbh
    if path:
        print(f"Path from {start_location} to {destination} using {algorithm}: {path}")
    else:
        print(f"No path found from {start_location} to {destination} using {algorithm}.")

# runs main func
if __name__ == "__main__":
    main()