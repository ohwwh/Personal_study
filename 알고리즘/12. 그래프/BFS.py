from collections import deque
from collections import defaultdict
graph1 = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}
graph2 = {4: [3, 2], 3: [4, 1, 2], 1: [3], 2: [4, 3]}


def BFS(graph, s):
    visited = [False] * (len(graph) + 1)
    visited[1] = True
    unprocessed = deque([s])
    ret = [s]
    while unprocessed:
        v = unprocessed.popleft()
        for u in graph[v]:
            if not visited[u]:
                unprocessed.append(u)
                visited[u] = True
                ret.append(u)
    return ret


print(BFS(graph2, 1))



