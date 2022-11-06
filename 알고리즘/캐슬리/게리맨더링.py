import sys
from itertools import combinations


N = int(sys.stdin.readline())

parr = list(map(int, sys.stdin.readline().split()))
graph = {}

for i in range(1, N + 1):
    arr = list(map(int, sys.stdin.readline().split()))
    graph[i] = []
    for j in range(1, arr[0] + 1):
        graph[i].append(arr[j])

def part(lst):
    ret = []
    for i in range(1, len(lst)):
        ret += list(map(list, combinations(lst, i)))
    return ret
    
def diff(lstA, lstB):
    ret = []
    for i in lstA:
        if i not in lstB:
            ret.append(i)
    return ret

def pop(vstd, parr):
    ret = 0
    for i in vstd:
        ret += parr[i - 1]
    return ret

def dfs(graph, s, visited):
    visited.append(s)
    for i in graph[s]:
        if i not in visited:
            dfs(graph, i, visited)

def is_conn(group, visited):
    ret = True
    visited_copy = visited[:]
    dfs(graph, group[0], visited_copy)
    if len(visited_copy) != N:
        ret = False
    return ret

min = 10000
wp = pop(list(range(1, N+1)), parr)

groups = part(list(range(1, N+1)))
for g in groups:
    visited = diff(list(range(1, N+1)), g)
    if is_conn(g, visited) == True:
        if is_conn(visited, g) == True:
            p = pop(g, parr)
            if abs(wp - 2*p) < min: 
                min = abs(wp - 2*p)

if min == 10000:
    min = -1

print(min)