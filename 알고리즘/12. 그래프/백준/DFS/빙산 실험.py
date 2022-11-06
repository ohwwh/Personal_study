import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
grid = []
iceberg_list = []
j = 0
for _ in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    grid.append(l)
    for i in range(m):
        if grid[j][i] != 0:
            iceberg_list.append((i, j))
    j += 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



def dfs(nums):
    melting_area = {}
    visited = [[False] * m for _ in range(n)]
    visited[iceberg_list[0][1]][iceberg_list[0][0]] = True
    cnt = 0
    stack = []
    stack.append(iceberg_list[0])
    while stack:
        x, y = stack.pop()
        cnt += 1
        mcnt = 0
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if not visited[yy][xx] and nums[yy][xx] != 0:
                visited[yy][xx] = True
                stack.append((xx, yy))
            if nums[y][x] > 0 and nums[yy][xx] == 0:
                mcnt += 1

        melting_area[(x, y)] = mcnt

    new_iceberg_list = []
    for key, value in melting_area.items():
        i, j = key
        grid[j][i] = max(0, grid[j][i] - value)
        if grid[j][i] > 0:
            new_iceberg_list.append((i, j))
    return cnt, new_iceberg_list


year = 0
while True:
    cnt, new_iceberg = dfs(grid)
    if cnt != len(iceberg_list):
        break
    if cnt == 0 or not new_iceberg:
        year = 0
        break
    year += 1
    iceberg_list = new_iceberg[:]

print(year)

