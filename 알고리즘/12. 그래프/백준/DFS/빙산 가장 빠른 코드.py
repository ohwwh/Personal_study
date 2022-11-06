import sys

sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
grid = []
iceberg_list = []
new_iceberg_list = []
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

cnt = [0]


def dfs(x, y, nums, nums2):
    visited[y][x] = True
    cnt[0] += 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if 0 <= xx < m and 0 <= yy < n:
            if not visited[yy][xx] and nums[yy][xx] != 0:
                dfs(xx, yy, nums, nums2)
            if nums[y][x] > 0 and nums2[yy][xx] == 0:
                nums[y][x] -= 1

year = 0
while True:
    grid2 = [item[:] for item in grid]
    if not iceberg_list:
        year = 0
        break
    s = iceberg_list[0]
    cnt[0] = 0
    visited = [[False] * m for _ in range(n)]
    dfs(s[0], s[1], grid, grid2)
    if cnt[0] != len(iceberg_list):
        break
    for t in iceberg_list:
        if grid[t[1]][t[0]] != 0:
            new_iceberg_list.append((t[0], t[1]))
    year += 1
    iceberg_list = new_iceberg_list[:]
    new_iceberg_list = []

print(year)
