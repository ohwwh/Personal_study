import sys
import collections
sys.setrecursionlimit(10000000)

n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def connectedcomponenet(graph):
    visited = [False] * (n+1)
    cnt = 0

    def dfs(u):
        if not visited[u]:
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    dfs(v)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    return cnt - visited.count(True)


print(connectedcomponenet(graph) + n)