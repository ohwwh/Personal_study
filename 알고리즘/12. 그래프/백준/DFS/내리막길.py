import sys
sys.setrecursionlimit(10000000000)
m, n = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]



'''4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10'''

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * n for _ in range(m)]
visited[0][0] = True
path = [0]


def dfs(x, y):
    if x == n-1 and y == m-1:
        path[0] += 1
        return
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if 0 <= xx < n and 0 <= yy < m and not visited[yy][xx] and grid[y][x] > grid[yy][xx]:
            visited[yy][xx] = True
            dfs(xx, yy)
            visited[yy][xx] = False


dfs(0, 0)
print(path[0])
