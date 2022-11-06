import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
if n == k:
    print(0)
elif k < n:
    print(n - k)
else:
    sec = [0] * (2 * k)
    unprocessed = deque([n])
    visited = [False] * (2 * k)
    visited[n] = True

    while sec[k] == 0:
        v = unprocessed.popleft()
        if 0 <= v + 1 <= 2 * k - 1 and (sec[v + 1] == 0 or sec[v] + 1 < sec[v + 1]):
            unprocessed.append(v + 1)
            sec[v + 1] = sec[v] + 1
        if 0 <= v - 1 <= 2 * k - 1 and (sec[v - 1] == 0 or sec[v] + 1 < sec[v - 1]):
            unprocessed.append(v - 1)
            sec[v - 1] = sec[v] + 1
        if 0 <= v * 2 <= 2 * k - 1 and (sec[v * 2] == 0 or sec[v] + 1 < sec[v * 2]):
            unprocessed.append(v * 2)
            sec[v * 2] = sec[v] + 1

    unprocessed.clear()

    print(sec[k])
