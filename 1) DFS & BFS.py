def create_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        edge = input("Enter edge (node1 node2): ").split()
        node, neighbour = edge[0], edge[1]
        if node in graph:
            graph[node].append(neighbour)
        else:
            graph[node] = [neighbour]
        if neighbour not in graph:
            graph[neighbour] = []
    return graph

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node):
    visited.add(node)
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Driver code
graph = create_graph()
start_node = input("Enter the start node: ")
print("Following is the DFS:")
dfs(set(), graph, start_node)
print("\nFollowing is the BFS:")
bfs(set(), graph, start_node)


"""

Output:

Enter the number of edges: 4
Enter edge (node1 node2): A B
Enter edge (node1 node2): B C
Enter edge (node1 node2): B D
Enter edge (node1 node2): D E
Enter the start node: A

Following is the DFS:
A
B
C
D
E

Following is the BFS:
A B C D E

"""



