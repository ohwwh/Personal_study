import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min = [10000];
team1 = list(range(N))
team2 = []

def stat(arr, team, n):
    ret = 0
    for i in range(n):
        for j in range(i + 1, n):
            ret += (arr[team[i]][team[j]] + arr[team[j]][team[i]])
    return ret

def Comb(depth, start, N, team1, team2):
    if depth == N / 2:
        dif = abs(stat(arr, team1, int(N/2)) - stat(arr, team2, int(N/2)))
        if dif < min[0]:
            min[0] = dif
        return
    for i in range(start, N):
        team2.append(i)
        team1.remove(i)
        Comb(depth + 1, i + 1, N, team1, team2)
        team2.remove(i)
        team1.append(i)

Comb(0, 0, N, team1, team2)
print(min[0])
