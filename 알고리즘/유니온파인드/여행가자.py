import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parent = [0] * (N + 1)
level = [1] * (N + 1)
for i in range(1, N + 1):
	parent[i] = i

def find(u):
	if u == parent[u]:
		return u
	parent[u] = find(parent[u]) # 경로 압축 최적화
	return parent[u]

def union(b, c):
	b = find(b)
	c = find(c)

	if b == c:
		return
	if level[b] > level[c]:
		parent[c] = b
		level[b] += level[c]
	else:
		parent[b] = c
		level[c] += level[b]

for i in range(1, N + 1):
	l = list(map(int, sys.stdin.readline().split()))
	for j in range(0, N):
		if l[j] == 1:
			union(i, j + 1)

p = list(map(int, sys.stdin.readline().split()))
f = find(p[0])
for k in p[1:]:
	if f != find(k):
		print("NO")
		exit()

print("YES")