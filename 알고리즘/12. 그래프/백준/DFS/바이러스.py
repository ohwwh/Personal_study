import sys
from collections import defaultdict
num = int(sys.stdin.readline())
pair = int(sys.stdin.readline())
graph1 = defaultdict(list)
for i in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    graph1[a].append(b)
    graph1[b].append(a)

#graph1 = collections.defaultdict(list, {1: [2, 5], 2: [3], 5: [2, 6], 4: [7]})
#graph1 = collections.defaultdict(list, {1: [2, 5], 5: [2]})
#graph1 = collections.defaultdict(list, {1: [], 2: [3], 5: [2, 6], 4: [7]})

visited = [False] * (num+1)

def virus(graph):
    cnt = [0]
    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                cnt[0] += 1
                dfs(v)

    dfs(1)
    return cnt[0]


print(virus(graph1))
