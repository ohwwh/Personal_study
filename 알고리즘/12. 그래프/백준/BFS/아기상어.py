from collections import deque
import sys
import heapq
import copy

n = int(sys.stdin.readline())
grid = []
k = 0
for _ in range(n):
    e = list(map(int, sys.stdin.readline().split()))
    grid.append(e)
    if 9 in e:
        sh = (0, e.index(9), k)

    k += 1

grid[sh[2]][sh[1]] = 0

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

#visited_mother = [[False] * n for _ in range(n)]
def shark(nums, start):
    #lengthgrid_mother = [[0] * n for _ in range(n)]

    def shortest(s, size):
        mn = 100000000000000
        #visited = copy.deepcopy(visited_mother)
        visited = [[False] * n for _ in range(n)]
        #lengthgrid = copy.deepcopy(lengthgrid_mother)
        lengthgrid = [[0] * n for _ in range(n)]
        unprocessed = deque([s])
        visited[s[2]][s[1]] = True
        tlist = []
        while unprocessed:
            v = unprocessed.popleft()
            for i in range(4):
                a, b, length = v[1] + dx[i], v[2] + dy[i], v[0]
                if 0 <= a < n and 0 <= b < n and nums[b][a] <= size and not visited[b][a]:
                    visited[b][a] = True
                    length += 1
                    if 0 < nums[b][a] < size:
                        mn = length
                        tlist.append((mn, b, a))
                    if length <= mn:
                        unprocessed.append((length, a, b))
        if tlist:
            tlist.sort()
            nums[tlist[0][1]][tlist[0][2]] = 0
            return tlist[0]
        else:
            return -1

    size = 2
    cnt = 0
    sec = 0
    while True:
        temp = shortest(start, size)
        if temp == -1:
            return sec
        else:
            goal = (0, temp[2], temp[1])
            mn = temp[0]
        sec += mn
        start = goal
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0

    return sec


print(shark(grid, sh))
