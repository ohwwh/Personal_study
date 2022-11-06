import sys, copy

sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def around(x, y, nums):
    cnt = 0
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if nums[y][x] != 0 and 0 <= xx < m and 0 <= yy < n and nums[yy][xx] == 0:
            cnt += 1

    ret = (x, y, cnt)
    return ret


def iceberg(nums):
    visited = [[False] * m for _ in range(n)]
    # nums2 = copy.deepcopy(nums)

    def dfs(x, y):
        visited[y][x] = True
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < m and 0 <= yy < n and not visited[yy][xx] and nums[yy][xx] != 0:
                dfs(xx, yy)
            '''if 0 <= xx < m and 0 <= yy < n and nums[y][x] != 0 and nums2[yy][xx] == 0:
                nums[y][x] -= 1'''

    cnt = 0
    for i in range(m):
        for j in range(n):
            if nums[j][i] != 0 and not visited[j][i]:
                dfs(i, j)
                cnt += 1
    return cnt


year = 0
melting_list = []
while True:
    ret = iceberg(grid)
    if ret > 1:
        break
    if ret == 0:
        year = 0
        break
    for i in range(m):
        for j in range(n):
            if grid[j][i] != 0:
                melting_list.append(around(i, j, grid))
    while melting_list:
        x, y, count = melting_list.pop()
        grid[y][x] -= count
        if grid[y][x] < 0:
            grid[y][x] = 0
    year += 1

print(year)
