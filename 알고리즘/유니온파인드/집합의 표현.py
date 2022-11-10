import sys

n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n + 1)
level = [1] * (n + 1)
ret = []
for i in range(1, n + 1):
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

for _ in range(m):
	a, b, c = map(int, sys.stdin.readline().split())
	if a == 0:
		union(b, c)
	else:
		if find(b) == find(c):
			ret.append(1)
		else:
			ret.append(0)

for e in ret:
	if e == 1:
		print("yes")
	else:
		print("no")