import sys
sys.setrecursionlimit(10**6)
v = int(input())

tree = [[] for _ in range(v)]

for _ in range(v):
	tmp = list(map(int, input().split()))
	for i in range(1, len(tmp) - 1):
		tree[tmp[0] - 1].append(tmp[i])
	tree[tmp[0] - 1].append(len(tmp) - 2)


distance = [0] * v

def DFSvisit(tree, d, u):
	for i in range(tree[u][-1]):
		if i % 2 == 0 and d[tree[u][i] - 1] == 0:
			d[tree[u][i] - 1] = d[u] + tree[u][i + 1]
			DFSvisit(tree, d, tree[u][i] - 1)

DFSvisit(tree, distance, 0)
distance[0] = 0
midx = 0
for i in range(v):
	if distance[i] > distance[midx]:
		midx = i

distance2 = [0] * v
DFSvisit(tree, distance2, midx)
distance2[midx] = 0

print(max(distance2))