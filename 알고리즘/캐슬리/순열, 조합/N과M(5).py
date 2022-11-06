from itertools import combinations_with_replacement

N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

p = combinations_with_replacement(lst, M)

for e in p:
	for i in e:
		print(i,end=' ')
	print("\n",end='')