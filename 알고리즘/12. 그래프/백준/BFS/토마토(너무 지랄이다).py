from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())
cube = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def tomato(nums):
    visited = [[[False] * m for _ in range(n)] for _ in range(h)]
    slist = []
    for i in range(n):
        for j in range(h):
            slist = slist + nums[j][i]
    cnt = [slist.count(0)]

    def bfs(s):
        move = 0
        if nums[s[2]][s[1]][s[0]] != 1 or visited[s[0]][s[1]][s[2]]:
            return -1
        visited[s[0]][s[1]][s[2]] = True
        for i in range(6):
            a, b, c = s[0] + dx[i], s[1] + dy[i], s[2] + dz[i]
            if 0 <= a < m and 0 <= b < n and 0 <= c < h and nums[c][b][a] == 0:
                nums[c][b][a] = 1
                cnt[0] -= 1
                if not move:
                    move = 1
        return move

    day = 0
    while True:
        for i in range(m):
            for j in range(n):
                for k in range(h):
                    t = bfs([i, j, k])
                    if t != -1:
                        if t == 0:
                            if cnt[0] == 0:
                                return day
                            else:
                                return -1
        day += 1







print(tomato(cube))
