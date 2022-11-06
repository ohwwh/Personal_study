import sys
sys.setrecursionlimit(10000)

j, i = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(j)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def outer(x, y, i, j, arr, p):
    if x < 0 or y < 0 or x >= i or y >= j:
        return
    if arr[y][x] == 1 or arr[y][x] == -p:
        return
    arr[y][x] = -p
    outer(x + 1, y, i, j, arr, p)
    outer(x - 1, y, i, j, arr, p)
    outer(x, y + 1, i, j, arr, p)
    outer(x, y - 1, i, j, arr, p)


def process(arr, p):
    cheese = 0
    for k in range(j):
        for l in range(i):
            if arr[k][l] == 1:
                for n in range(4):
                    if k + dy[n] >= 0 and k + dy[n] < j and l + dx[n] >= 0 and l + dx[n] < i:
                        if arr[k + dy[n]][l + dx[n]] == -p:
                            arr[k][l] = -p - 1
                            break
                cheese += 1
    for k in range(j):
        for l in range(i):
            if arr[k][l] == -p - 1:
                arr[k][l] = -p
    return cheese

n = 1
p = 1

while (n != 0):
    outer(0, 0, i, j, arr, p)
    n = process(arr, p)
    if n == 0:
        print(p - 1)
        print(m)
        break
    m = n
    p += 1