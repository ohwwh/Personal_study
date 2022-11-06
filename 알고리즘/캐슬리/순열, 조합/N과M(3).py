from itertools import product

N, M = map(int, input().split())

p = product(range(1, N+1), repeat = M)

for e in p:
	for i in e:
		print(i,end=' ')
	print("\n",end='')