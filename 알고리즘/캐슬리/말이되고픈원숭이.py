import sys
import copy
from collections import deque

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
visited = [list([0]*W for _ in range(H)) for _ in range(31)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dnx = [-1, -2, 1, 2, -1, -2, 1, 2]
dny = [-2, -1, -2, -1, 2, 1, 2, 1]

def bfs():
    queue = deque([(0, 0, 0)])
    while queue:
        v = queue.pop()
        s, x, y = v[0], v[1], v[2]
        if x == W - 1 and y == H - 1:
            return (visited[s][y][x])
        for i in range(4):
            if x + dx[i] >= 0 and y + dy[i] >= 0 and x + dx[i] < W and y + dy[i] < H and arr[y + dy[i]][x + dx[i]] == 0 and visited[s][y + dy[i]][x + dx[i]] == 0:
                queue.appendleft((s, x + dx[i], y + dy[i]))
                visited[s][y + dy[i]][x + dx[i]] = visited[s][y][x] + 1
        for i in range(8):
            if s < K and x + dnx[i] >= 0 and y + dny[i] >= 0 and x + dnx[i] < W and y + dny[i] < H and arr[y + dny[i]][x + dnx[i]] == 0 and visited[s + 1][y + dny[i]][x + dnx[i]] == 0:
                queue.appendleft((s + 1, x + dnx[i], y + dny[i]))
                visited[s + 1][y + dny[i]][x + dnx[i]] = visited[s][y][x] + 1
    return (-1)



print(bfs())