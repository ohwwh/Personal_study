def count(arr):
        count = 0
        for i in range(W):
            for j in range(H):
                if arr[j][i] != 0:
                    count += 1
        return count

def stage(start, arr, n):
    k = 0
    while k < H and arr[k][start] == 0:
        k += 1
    if k == H:
        return -1
    first = (start, k)
    tobreak.append(first)
    visited = {first}
    while tobreak:
        f = tobreak.pop()
        n -= 1
        for i in range(1, arr[f[1]][f[0]]):
            if f[0] + i < W and arr[f[1]][f[0] + i] != 0 and (f[0] + i, f[1]) not in visited:
                tobreak.append((f[0] + i, f[1]))
                visited.add((f[0] + i, f[1]))
            if f[0] - i >= 0 and arr[f[1]][f[0] - i] != 0 and (f[0] - i, f[1]) not in visited:
                tobreak.append((f[0] - i, f[1]))
                visited.add((f[0] - i, f[1]))
            if f[1] + i < H and arr[f[1] + i][f[0]] != 0 and (f[0], f[1] + i) not in visited:
                tobreak.append((f[0], f[1] + i))
                visited.add((f[0], f[1] + i))
            if f[1] - i >= 0 and arr[f[1] - i][f[0]] != 0 and (f[0], f[1] - i) not in visited:
                tobreak.append((f[0], f[1] - i))
                visited.add((f[0], f[1] - i))
        arr[f[1]][f[0]] = 0
    return (n)

def fall(arr):
    for i in range(W):
        for j in range(H):
            if arr[j][i] != 0:
                stack.append(arr[j][i])
                arr[j][i] = 0
        j = H - 1
        while stack:
            arr[j][i] = stack.pop()
            j -= 1
            

def find_best(arr, N, n):
    global min
    if N == 0:
        return
    for s in range(W):
        arr_copy = [item[:] for item in arr]
        m = stage(s, arr_copy, n)
        if m != -1:
            fall(arr_copy)
            if min > m:
                min = m
            if min != 0:
                find_best(arr_copy, N - 1, m)

tobreak = []
stack = []

T = int(input())
for n in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    global min
    min = 180
    find_best(arr, N, count(arr))
    print("#%d %d" %(n, min))