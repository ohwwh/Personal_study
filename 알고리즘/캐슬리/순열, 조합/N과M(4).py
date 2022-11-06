from itertools import combinations_with_replacement

N, M = map(int, input().split())

p = combinations_with_replacement(range(1, N+1), M)

for e in p:
	for i in e:
		print(i,end=' ')
	print("\n",end='')