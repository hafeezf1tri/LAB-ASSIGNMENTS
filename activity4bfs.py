def bfs(graph, start, goal):
    visited = []
    queue = [start]
    
    while queue:
        print("Visited: ", visited)
        print("Queue: ", queue)
        current = queue.pop(0)
        
        if current == goal:
            visited.append(current)
            break
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
        
        visited.append(current)
    
    return visited

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
    'G': set(['J', 'I']),
    'L': set(['J']),
    'K': set(['I'])
}

# Example usage of BFS
start_node = 'S'
goal_node = 'H'
path = bfs(graph_03, start_node, goal_node)

print(f"Path from {start_node} to {goal_node}: {path}")