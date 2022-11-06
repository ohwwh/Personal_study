import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def worm(nums, s):
    if nums[s[1]][s[0]] != 1:
        return False
    nums[s[1]][s[0]] = -1
    unprocessed = deque([s])
    visited = [[False] * m for _ in range(n)]
    while unprocessed:
        v = unprocessed.popleft()
        x, y = v[0], v[1]
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < m and 0 <= b < n and nums[b][a] == 1 and (a, b) and not visited[b][a]:
                visited.append((a, b))
                unprocessed.append((a, b))
                nums[b][a] = -1
    return True


t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    grid = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        grid[y][x] = 1

    cnt = 0

    for i in range(m):
        for j in range(n):
            if worm(grid, (i, j)):
                cnt += 1

    print(cnt)





