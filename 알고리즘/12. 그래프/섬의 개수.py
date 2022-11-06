'''while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]'''

graph1 = [[1, 0, 1, 0, 0], [1, 0, 0, 0, 0], [1, 0, 1, 0, 1], [1, 0, 0, 1, 0]]
graph2 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
graph3 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]


def found(graph):
    cnt = 0
    w = len(graph[0])
    h = len(graph)

    def dfs(graph, i, j):
        if i < 0 or j < 0 or i >= h or j >= w or graph[i][j] == 0:
            return False
        else:
            graph[i][j] = 0
            dfs(graph, i - 1, j)
            dfs(graph, i + 1, j)
            dfs(graph, i, j - 1)
            dfs(graph, i, j + 1)
            '''dfs(graph, i - 1, j + 1)
            dfs(graph, i - 1, j - 1)
            dfs(graph, i + 1, j + 1)
            dfs(graph, i + 1, j - 1)'''
            return True

    for i in range(h):
        for j in range(w):
            if dfs(graph, i, j) is True:
                cnt += 1

    return cnt


print(found(graph1))
print(found(graph2))
print(found(graph3))
