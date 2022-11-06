import sys
import collections

n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def connectedcomponents(nums):
    visited = [False] * (n+1)
    vcnt = [0]

    def bfs(s):
        if visited[s]:
            return False
        visited[s] = True
        vcnt[0] += 1
        unprocessed = collections.deque([s])
        while unprocessed:
            v = unprocessed.popleft()
            for u in nums[v]:
                if not visited[u]:
                    unprocessed.append(u)
                    visited[u] = True
                    vcnt[0] += 1

        return True

    cnt = 0
    for i in list(nums):
        if bfs(i):
            cnt += 1

    return cnt + n - vcnt[0]


print(connectedcomponents(graph))

