import collections
import copy

schedule1 = [[1, 0], [0, 1]]
schedule2 = [[1, 0]]
schedule3 = [[0, 1], [0, 2], [1, 2]]
schedule4 = [[5, 5]]
schedule5 = [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
coursecnt = 2


def courseschedule(schedule):
    graph = collections.defaultdict(list)
    for a, b in schedule:
        graph[a].append(b)

    visited = []
    processed = set()

    def dfs(u):
        if u in visited:
            return False
        if u in processed:
            return True
        visited.append(u)
        processed.add(u)
        for v in graph[u]:
            if not dfs(v):
                return False
        visited.remove(u)
        return True

    for i in list(graph):
        if not dfs(i):
            return False
    return True


print(courseschedule(schedule4))
