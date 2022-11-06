import sys
from collections import deque
import copy

grid = []
mx = 0
mn = 101
n = int(sys.stdin.readline())
for _ in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    mx = max(mx, max(l))
    mn = min(mn, min(l))
    grid.append(l)




'''n = 5
grid = [[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2], [7, 2, 5, 3, 6], [8, 9, 5, 2, 7]]
h = 0'''

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def safezone(grid, nums, h):
    nums = copy.deepcopy(grid)
    visited = [[False] * n for _ in range(n)]

    def bfs(s):
        if nums[s[1]][s[0]] == -1 or nums[s[1]][s[0]] <= h:
            return False
        nums[s[1]][s[0]] == -1
        unprocessed = deque([s])

        while unprocessed:
            v = unprocessed.popleft()
            for i in range(4):
                a, b = v[0] + dx[i], v[1] + dy[i]
                if 0 <= a < n and 0 <= b < n and nums[b][a] > h and not visited[b][a]:
                    unprocessed.append((a, b))
                    visited[b][a] = True
                    nums[b][a] = -1

        return True

    cnt = 0

    for i in range(n):
        for j in range(n):
            if bfs((i, j)):
                cnt += 1

    nums.clear()
    return cnt


'''ret = set()
for i in list(map(set, grid)):
    ret = ret | i
ret = list(ret)'''

gridcopy = []
mxret = 0
for i in range(mn, mx):
    mxret = max(mxret, safezone(grid, gridcopy, i))

if mxret == 0:
    mxret = 1

print(mxret)
