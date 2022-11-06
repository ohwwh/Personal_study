import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

if n == k:
    print(0)
else:
    l = max(n, k)
    sec = [0] * (2 * l)
    unprocessed = deque([n])
    visited = [False] * (2 * l)
    visited[n] = True

    while sec[k] == 0:
        v = unprocessed.popleft()
        if 0 <= v + 1 <= 2 * l - 1 and (sec[v + 1] == 0 or not visited[v + 1]):
            unprocessed.append(v + 1)
            sec[v + 1] = sec[v] + 1
            visited[v + 1] = True
        if 0 <= v - 1 <= 2 * l - 1 and (sec[v - 1] == 0 or not visited[v - 1]):
            unprocessed.append(v - 1)
            sec[v - 1] = sec[v] + 1
            visited[v - 1] = True
        if 0 <= v * 2 <= 2 * l - 1 and (sec[v * 2] == 0 or not visited[v * 2]):
            unprocessed.append(v * 2)
            sec[v * 2] = sec[v] + 1
            visited[v * 2] = True

    unprocessed.clear()

    print(sec[k])


