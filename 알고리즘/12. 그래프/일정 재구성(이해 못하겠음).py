import collections
path1 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
path2 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
path3 = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]


def Itinerary(path, start):
    graph = collections.defaultdict(list)
    for a, b in path:
        graph[a].append(b)
    for a in graph:
        graph[a].sort()
    visited = []

    def dfsvisit(u):
        while graph[u]:
            dfsvisit(graph[u].pop(0))
        visited.append(u)


    dfsvisit(start)
    return visited[::-1]


print(Itinerary(path3, 'JFK'))
