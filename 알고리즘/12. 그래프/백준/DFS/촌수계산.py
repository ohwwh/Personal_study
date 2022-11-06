import sys
from collections import defaultdict

n = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)


def dfs(s, g):
    if s == g or not graph[s]:
        return
    for v in graph[s]:
        if not visited[v]:
            visited[v] = visited[s] + 1
            dfs(v, g)

def dfsstack(s, g):
    stack = []
    stack.append(s)
    while stack:
        u = stack.pop()
        if u == g:
            break
        for v in graph[u]:
            if not visited[v]:
                visited[v] = visited[u] + 1
                stack.append(v)


dfsstack(x, y)

if visited[y] == 0:
    ret = -1
else:
    ret = visited[y]

print(ret)
