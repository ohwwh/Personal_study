import sys, copy
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def iceberg(nums):
    visited = [[False] * m for _ in range(n)]
    nums2 = [item[:] for item in nums]
    visited[grid[0][1]][grid[0][0]] = True

    def dfs(x, y):
        visited[y][x] = True
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < m and 0 <= yy < n:
                if not visited[yy][xx] and nums2[yy][xx] != 0:
                    dfs(xx, yy)
                if nums[y][x] != 0 and nums2[yy][xx] == 0:
                    nums[y][x] -= 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if nums[j][i] != 0 and not visited[j][i]:
                dfs(i, j)
                cnt += 1
    return cnt


year = 0
while True:
    ret = iceberg(grid)
    if ret > 1:
        break
    if ret == 0:
        year = 0
        break
    year += 1

print(year)
