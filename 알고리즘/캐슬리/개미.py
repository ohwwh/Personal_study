import sys

w, h = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))
t = int(sys.stdin.readline())
ret = [0, 0]

if int((p[0] + t) / w) % 2 == 0:
    ret[0] = (p[0] + t) % w
else:
    ret[0] = w - ((p[0] + t) % w)

if int((p[1] + t) / h) % 2 == 0:
    ret[1] = (p[1] + t) % h
else:
    ret[1] = h - ((p[1] + t) % h)

print(ret[0], ret[1])