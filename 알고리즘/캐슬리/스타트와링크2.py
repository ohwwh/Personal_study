import sys
from itertools import combinations

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min = 10000;
team1 = list(range(N))
team2 = []

def stat(arr, team, n):
    ret = 0
    for i in range(n):
        for j in range(i + 1, n):
            ret += (arr[team[i]][team[j]] + arr[team[j]][team[i]])
    return ret

comb = list(combinations(team1, int(N/2)))

for i in comb:
    for j in range(int(N/2)):
        team1.remove(i[j])
    dif = abs(stat(arr, team1, int(N/2)) - stat(arr, i, int(N/2)))
    if dif < min:
        min = dif
    for j in range(int(N/2)):
        team1.append(i[j])

print(min)
