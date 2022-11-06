graph1 = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}


def DFS(graph, s):
    visited = []
    tovisit = [s]
    while tovisit:
        u = tovisit.pop()
        visited.append(u)
        for v in graph[u]:
            if v not in visited + tovisit:
                tovisit.append(v)
    return visited


print(DFS(graph1, 1))
