from collections import deque
import sys

n = int(sys.stdin.readline())
nums = []
k = 0
fish_cnt = 0
for _ in range(n):
    e = list(map(int, sys.stdin.readline().split()))
    nums.append(e)
    if 9 in e:
        sh = (0, e.index(9), k)
    for i in e:
        if 0 < i <= 6:
            fish_cnt += 1

    k += 1

nums[sh[2]][sh[1]] = 0

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


def shortest(s):
    mn = 100000000000000
    visited = [[False] * n for _ in range(n)]
    unprocessed = deque([s])
    visited[s[2]][s[1]] = True
    tlist = []
    cnt = 0
    while unprocessed:
        v = unprocessed.popleft()
        for i in range(4):
            a, b, length = v[1] + dx[i], v[2] + dy[i], v[0]
            if 0 <= a < n and 0 <= b < n and nums[b][a] <= size and not visited[b][a]:
                visited[b][a] = True
                if 0 < nums[b][a] < size:
                    if cnt == 0:
                        mn = length + 1
                    tlist.append((length + 1, b, a))
                    cnt += 1
                if length + 1 <= mn:
                    unprocessed.append((length + 1, a, b))
    if tlist:
        tlist.sort()
        return tlist[0]
    else:
        return -1


size = 2
cnt = 0
sec = 0

while fish_cnt:
    temp = shortest(sh)
    if temp == -1:
        break
    else:
        goal = (0, temp[2], temp[1])
        mn = temp[0]
    sec += mn
    sh = goal
    cnt += 1
    fish_cnt -= 1
    if cnt == size:
         size += 1
         cnt = 0
    nums[sh[2]][sh[1]] = 0

print(sec)
