
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    
    path.append(start)
    
    if start == goal:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in path:
            result = dfs(graph, neighbor, goal, path)
            if result:
                return result
    
    path.pop()
    return None

# Define the updated graph using sets for the adjacency list
graph_dfs = {
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
    'G': set(['J', 'I']),
    'L': set(['J']),
    'K': set(['I'])
}

start_node = 'S'
goal_node = 'K'
path = dfs(graph_dfs, start_node, goal_node)

print(f"Path from {start_node} to {goal_node}: {path}")