import sys

N, M, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
k = 1;
TN, TM = N, M


def rotate(M, N, arr, k):
    k -= 1
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

while TM > 0 and TN > 0:
    for _ in range(int(R % (2 * (TM + TN - 2)))):
        rotate(TN, TM, arr, k)
    k += 1
    TM -= 2
    TN -= 2

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()