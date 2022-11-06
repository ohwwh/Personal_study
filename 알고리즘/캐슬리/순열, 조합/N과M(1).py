from itertools import permutations

N, M = map(int, input().split())

p = list(permutations(range(1, N + 1), M))

for e in p:
	for i in e:
		print(i,end=' ')
	print("\n",end='')
