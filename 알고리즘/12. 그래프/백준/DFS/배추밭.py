import sys
sys.setrecursionlimit(10**6)

def worm(grid):
    cnt = 0

    def dfs(x, y):
        if x >= n or y >= m or x < 0 or y < 0 or grid[x][y] == 0:
            return False
        else:
            grid[x][y] = 0
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            return True

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                cnt += 1

    return cnt


T = int(sys.stdin.readline())
for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    grid = [[0] * m for i in range(n)]
    for _ in range(k):
        i, j = map(int, sys.stdin.readline().split())
        grid[j][i] = 1
    print(worm(grid))

