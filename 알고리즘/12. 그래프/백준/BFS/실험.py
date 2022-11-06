import sys
import collections

n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def connectedcomponents(nums):
    visited = []
    vcnt = [0]

    def bfs(s):
        if s in visited:
            return False
        visited.append(s)
        vcnt[0] += 1
        unprocessed = collections.deque([s])
        while unprocessed:
            v = unprocessed.popleft()
            for u in nums[v]:
                if u not in visited:
                    unprocessed.append(u)
                    visited.append(u)
                    vcnt[0] += 1

        return True

    cnt = 0
    for i in list(nums):
        if bfs(i):
            cnt += 1

    return cnt + n - vcnt[0]


print(connectedcomponents(graph))

