import sys

n = int(sys.stdin.readline())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

room.sort(key = lambda x: (x[1], x[0]))

cnt = 1
m = room[0][1]
for i in range(1, n):
    if room[i][0] >= m:
        cnt += 1
        m = room[i][1]

print(cnt)