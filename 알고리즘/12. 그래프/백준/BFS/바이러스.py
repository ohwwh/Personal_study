import sys
from collections import defaultdict
from collections import deque
num = int(sys.stdin.readline())
pair = int(sys.stdin.readline())
graph1 = defaultdict(list)
for i in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    graph1[a].append(b)
    graph1[b].append(a)

#graph1 = defaultdict(list, {1: [2, 5], 2: [3], 5: [2, 6], 4: [7]})
#num = 7
#graph1 = defaultdict(list, {1: [2, 3], 2: [1, 3], 3: [1, 2]})
#num = 3
#graph1 = defaultdict(list, {1: [], 2: [3], 5: [2, 6], 4: [7]})
#num = 7
#graph1 = {4: [3, 2], 3: [4, 1, 2], 1: [3], 2: [4, 3]}
#num = 4


def virus(graph):
    visited = [False] * (num + 1)
    visited[1] = True
    unprocessed = deque([1])
    cnt = 0
    while unprocessed:
        v = unprocessed.popleft()
        cnt += 1
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                unprocessed.append(u)

    return cnt - 1


print(virus(graph1))
