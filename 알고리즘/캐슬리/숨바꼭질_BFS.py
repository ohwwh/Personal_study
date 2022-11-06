from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

if (N >= K):
    print(N - K)
    exit()

t = 1
visited = [False] * (2 * K)
visited[N] = True
unprocessed = deque([deque([N])])

while unprocessed[0]:
    unprocessed.append(deque())
    while unprocessed[0]:
        v = unprocessed[0].popleft()
        for u in [v - 1, v + 1, 2 * v]:
            if u < 0 or u > 2 * K - 1:
                continue
            if not visited[u]:
                if u == K:
                    print(t)
                    exit()
                unprocessed[1].append(u)
                visited[u] = True
    unprocessed.popleft()
    t += 1
