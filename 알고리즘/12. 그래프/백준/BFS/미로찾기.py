import sys
from collections import deque
from collections import defaultdict

m, n = map(int, sys.stdin.readline().split())
grid = []
for i in range(m):
    grid.append(list(sys.stdin.readline()))

grid[0][0] = 1

'''grid[i].pop()
    grid[i] = list(map(int, grid[i]))'''
'''grid = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
n = 6
m = 4'''


def maze(nums, n, m):
    unprocessed = deque([(0, 0)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    parents = defaultdict(int)
    path = deque()
    while unprocessed:
        v = unprocessed.popleft()
        if v == (n - 1, m - 1):
            break
        for i in range(4):
            x = v[0] + dx[i]
            y = v[1] + dy[i]
            if 0 <= x < n and 0 <= y < m and nums[y][x] == '1':
                unprocessed.append((x, y))
                nums[y][x] = nums[v[1]][v[0]] + 1
                parents[(x, y)] = (v[0], v[1])

    temp = ["답이 없는 미로요"]
    cur = (n-1, m-1)
    while cur != (0, 0):
        path.appendleft(cur)
        cur = parents[cur]
        if cur == 0:
            return temp
    path.appendleft((0, 0))

    #return nums[m - 1][n - 1]
    return list(path)


print(maze(grid, n, m))
