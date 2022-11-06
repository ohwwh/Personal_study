import sys
import copy
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
'''n = 7
grid1 = [[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2], [7, 2, 5, 3, 6], [8, 9, 5, 2, 7]]
grid2 = [[9, 9, 9, 9, 9, 9, 9], [9, 2, 1, 2, 1, 2, 9], [9, 1, 8, 7, 8, 1, 9], [9, 2, 7, 9, 7, 2, 9],
         [9, 1, 8, 7, 8, 1, 9], [9, 2, 1, 2, 1, 2, 9], [9, 9, 9, 9, 9, 9, 9]]'''


def safezone(grid, h):
    zone = copy.deepcopy(grid)
    visited = []
    cnt = 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= n or j >= n or zone[i][j] == -1 or zone[i][j] <= h:
            return False
        else:
            zone[i][j] = -1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return True

    for i in range(n):
        for j in range(n):
            if dfs(i, j):
                cnt += 1
    return cnt


ret = set()
for i in list(map(set, grid)):
    ret = ret | i
ret = list(ret)

mx = 0
for i in ret:
    mx = max(mx, safezone(grid, i))

if mx == 0:
    mx = 1

print(mx)
