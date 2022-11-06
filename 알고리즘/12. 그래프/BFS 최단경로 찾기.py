from collections import deque
from collections import defaultdict

graph1 = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}
graph2 = defaultdict(list, {1: [2, 3], 2: [5], 3: [4], 4: [5], 5: [7]})



def BFSpath(graph, s, e):
    visited = list()
    parents = {}
    unprocessed = deque([s])
    ret = [s]
    path = deque()
    while unprocessed:
        v = unprocessed.popleft()
        if v == e:
            break
        for u in graph[v]:
            if u not in visited:
                unprocessed.append(u)
                parents[u] = v
                visited.append(u)
                ret.append(u)

    cur = e
    while cur != s:
        path.appendleft(cur)
        cur = parents[cur]
    path.appendleft(s)

    return list(path)



print(BFSpath(graph1, 1, 7))
