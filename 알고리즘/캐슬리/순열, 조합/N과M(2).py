from itertools import combinations

N, M = map(int, input().split())

c = combinations(range(1, N+1), M)

for e in c:
	for i in e:
		print(i,end=' ')
	print("\n",end='')