import sys

n = int(sys.stdin.readline())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m = 1

room.sort(key = lambda x: (x[1], x[0]))
u = 0
i = u + 1

while i < n:
    if room[i][0] >= room[u][1]:
        m += 1
        u = i
    i += 1

print(m)