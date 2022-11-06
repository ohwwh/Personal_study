import sys
from collections import deque

n = int(sys.stdin.readline())
grid = [list(sys.stdin.readline()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def color(nums):
    visited = [[False] * n for _ in range(n)]

    def bfs(s):
        if visited[s[1]][s[0]]:
            return False
        unprocessed = deque([s])
        while unprocessed:
            v = unprocessed.popleft()
            for i in range(4):
                a, b = v[0] + dx[i], v[1] + dy[i]
                if 0 <= a < n and 0 <= b < n and nums[b][a] == nums[v[1]][v[0]] and not visited[b][a]:
                    visited[b][a] = True
                    unprocessed.append((a, b))

        return True

    cnt = 0
    for i in range(n):
        for j in range(n):
            if bfs((i, j)):
                cnt += 1

    return cnt


def colorforblind(nums):
    visited = [[False] * n for _ in range(n)]

    def bfs(s):
        if visited[s[1]][s[0]]:
            return False
        unprocessed = deque([s])
        while unprocessed:
            v = unprocessed.popleft()
            for i in range(4):
                a, b = v[0] + dx[i], v[1] + dy[i]
                if 0 <= a < n and 0 <= b < n and not visited[b][a]:
                    if nums[b][a] == nums[v[1]][v[0]] or (nums[v[1]][v[0]] == 'R' and nums[b][a] == 'G') \
                            or (nums[v[1]][v[0]] == 'G' and nums[b][a] == 'R'):
                        visited[b][a] = True
                        unprocessed.append((a, b))


        return True

    cnt = 0
    for i in range(n):
        for j in range(n):
            if bfs((i, j)):
                cnt += 1

    return cnt


print(color(grid))
print(colorforblind(grid))




