N, M = map(int, input().split())

arr = []
larr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

for _ in range(M):
    larr.append(list(map(int, input().split())))

'''def sum(arr, x1, y1, x2, y2):
    ret = 0
    for j in range(y1, y2 + 1):
        for i in range(x1, x2 + 1):
            ret +=arr[j - 1][i - 1]
    return ret

for e in larr:
    print(sum(arr, e[0], e[1], e[2], e[3]))'''

for i in range(N):
    for j in range(N):
        if i > 0 and j > 0:
            arr[i][j] = arr[i][j] + arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]
        elif i > 0 and j == 0:
            arr[i][j] = arr[i][j] + arr[i - 1][j]
        elif j > 0 and i == 0:
            arr[i][j] = arr[i][j] + arr[i][j - 1]

def sum(arr, x1, y1, x2, y2):
    if x1 > 1 and y1 > 1:
        return (arr[y2 - 1][x2 - 1] + arr[y1 - 2][x1 - 2] - arr[y2 - 1][x1 - 2] - arr[y1 - 2][x2 - 1])
    elif x1 > 1 and y1 == 1:
        return (arr[y2 - 1][x2 - 1] - arr[y2 - 1][x1 - 2])
    elif y1 > 1 and x1 == 1:
        return (arr[y2 - 1][x2 - 1] - arr[y1 - 2][x2 - 1])
    else:
        return (arr[y2 - 1][x2 - 1])

for e in larr:
    print(sum(arr, e[1], e[0], e[3], e[2]))