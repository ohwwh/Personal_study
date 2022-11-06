import sys
from collections import deque
import copy
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def virus(nums):
    area = 0

    def bfsv(u):
        if nums[u[1]][u[0]] != 2:
            return
        unprocessed = deque([u])
        while unprocessed:
            v = unprocessed.popleft()
            for i in range(4):
                a, b = v[0] + dx[i], v[1] + dy[i]
                if 0 <= a < m and 0 <= b < n and nums[b][a] == 0:
                    # visited[b][a] = True
                    unprocessed.append((a, b))
                    nums[b][a] = 2

    for i in range(m):
        for j in range(n):
            bfsv((i, j))

    for i in range(m):
        for j in range(n):
            if nums[j][i] == 0:
                area += 1

    return area


def wall(nums):
    colist = []
    for i in range(m):
        for j in range(n):
            if nums[j][i] == 0:
                colist.append((i, j))
    # rlist = []
    ret = []

    '''def dfs(clist):
        if len(clist) <= len(colist) - 3:
            ret.append(rlist[:])
            return
        for e in clist:
            nlist = clist[:]
            nlist.remove(e)
            rlist.append(e)
            dfs(nlist)
            rlist.pop()

    dfs(colist)'''
    ret = combinations(colist, 3)
    return ret


wlist = wall(grid)

mx = 0
'''wlist = []
for i in range(m):
    for j in range(n):
        if grid[j][i] == 0:
            wlist.append((i, j))

l = len(wlist)
for i in range(l):
    for j in range(i+1, l):
        for k in range(j+1, l):
            grid2 = copy.deepcopy(grid)
            grid2[wlist[i][1]][wlist[i][0]] = 1
            grid2[wlist[j][1]][wlist[j][0]] = 1
            grid2[wlist[k][1]][wlist[k][0]] = 1
            mx = max(mx, virus(grid2))'''

for e in wlist:
    grid2 = copy.deepcopy(grid)
    for v in e:
        grid2[v[1]][v[0]] = 1
    mx = max(mx, virus(grid2))

print(mx)
