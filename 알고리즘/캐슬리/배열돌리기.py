import sys

N, M, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def rotate(M, N, k, arr):
    if M <= 0 or N <= 0:
        return
    rotate(M - 2, N - 2, k + 1, arr)
    temp = arr[k][k]
    for i in range(N - 1):
        arr[k][k + i] = arr[k][k + i + 1]
    for i in range(M - 1):
        arr[k + i][k + N - 1] = arr[k + i + 1][k + N - 1]
    for i in range(N - 1):
        arr[k + M - 1][k + N - 1 - i] = arr[k + M - 1][k + N - 2 - i]
    for i in range(M - 1):
        arr[k + M - 1 - i][k] = arr[k + M - 2 - i][k]
    arr[k + 1][k] = temp

for _ in range(R):
    rotate(N, M, 0, arr)

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()