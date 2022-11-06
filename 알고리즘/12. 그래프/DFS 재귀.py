graph1 = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}

def DFSvisit(graph, visited, u):
    visited.append(u)
    for v in graph[u]:
        if v not in visited:
            DFSvisit(graph, visited, v)

def DFS(graph, s):
    discovered = []
    DFSvisit(graph, discovered, s)
    return discovered

print(DFS(graph1, 1))
