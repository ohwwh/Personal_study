import sys
from collections import defaultdict

sys.setrecursionlimit(1000000000)

n = int(sys.stdin.readline())
graph = defaultdict(list)
parents = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)


def dfs(u):
    if visited[u]:
        return False
    #visited[u] = True
    for v in graph[u]:
        #if not visited[v]:
            parents[v] = u
            dfs(v)

dfs(1)

for i in range(2, n+1):
    print(parents[i])
