import sys

n = int(input())
tower = list(map(int, sys.stdin.readline().split()))
ret = [0] * n
buf = [0]
buf[0] = n - 1
temp = 1

while temp != 0:
    temp = buf[-1] - 1
    while len(buf) != 0:
        i = 0
        if tower[temp] >= tower[buf[-1]]:
            ret[buf[-1]] = temp + 1
            buf.pop()
        else:
            break
    buf.append(temp)

for i in range(n):
    print(ret[i], end=' ')