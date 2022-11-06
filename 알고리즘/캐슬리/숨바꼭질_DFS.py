from collections import deque
import sys
sys.setrecursionlimit(10**6)

N, K = map(int, sys.stdin.readline().split())

visited = [False] * (K + N)
visited[N] = True

def recur(N, K, J, t, visited):
    min = 9999
    if (N == K):
        return t
    elif N < K and 2 * N < J:
        if not visited[2 * N]:
            visited[2 * N] = True
            m = recur(2 * N, K, J, t + 1, visited)
            if min > m:
                min = m
        if not visited[N + 1]:
            visited[N + 1] = True
            m = recur(N + 1, K, J, t + 1, visited)
            if min > m:
                min = m
    if N > 0 and not visited[N - 1]:
        visited[N - 1] = True
        m = recur(N - 1, K, J, t + 1, visited)
        if min > m:
            min = m
    return min


if (N >= K):
    print(N - K)
else:
    print(recur(N, K, K + N, 0, visited))
