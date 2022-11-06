from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())
cube = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]



def tomato(nums):
    '''slist = []
    for i in range(n):
        for j in range(h):
            slist = slist + nums[j][i]
    cnt = slist.count(0)
    if cnt == 0:
        return 0'''
    unprocessed = deque()
    mx = 0
    for i in range(m):
        for j in range(n):
            for k in range(h):
                if nums[k][j][i] == 1:
                    unprocessed.append([i, j, k])
    while unprocessed:
        s = unprocessed.popleft()
        for i in range(6):
            a, b, c = s[0] + dx[i], s[1] + dy[i], s[2] + dz[i]
            if 0 <= a < m and 0 <= b < n and 0 <= c < h and nums[c][b][a] == 0:
                unprocessed.append([a, b, c])
                nums[c][b][a] = nums[s[2]][s[1]][s[0]] + 1
                '''cnt -= 1
                if mx < nums[c][b][a]:
                    mx = nums[c][b][a]'''

    for i in range(m):
        for j in range(n):
            for k in range(h):
                if nums[k][j][i] == 0:
                    return -1
                mx = max(mx, nums[k][j][i])

    return mx - 1


print(tomato(cube))


