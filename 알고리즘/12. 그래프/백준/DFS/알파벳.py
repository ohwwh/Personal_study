import sys
from collections import defaultdict

r, c = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0] * c for _ in range(r)]
visited[0][0] = 1
alph = [0] * 26
alph[ord(grid[0][0])-65] = 1
mx = [1]


def dfs(x, y, visited):
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]

        if 0 <= xx < c and 0 <= yy < r and alph[ord(grid[yy][xx]) - 65] == 0:
            asci = ord(grid[yy][xx]) - 65
            visited[yy][xx] = visited[y][x] + 1
            mx[0] = max(mx[0], visited[yy][xx])
            alph[asci] = 1
            dfs(xx, yy, visited)
            alph[asci] = 0

def dfsstack(visited, alph):
    stack = []
    stack.append((0, 0))
    while stack:
        x, y = stack.pop()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < c and 0 <= yy < r and alph[ord(grid[yy][xx]) - 65] == 0:
                asci = ord(grid[yy][xx]) - 65
                visited[yy][xx] = visited[y][x] + 1
                mx[0] = max(mx[0], visited[yy][xx])
                alph[asci] = 1
                stack.append((xx, yy))
                alph[asci] = 0




dfsstack(visited, alph)

print(mx[0])
