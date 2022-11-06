N, M = map(int, input().split())

prnt = []
arr = list(map(int, input().split()))
for i in range (1, N):
	arr[i] = arr[i] + arr[i - 1]
for _ in range(M):
	i, j = map(int, input().split())
	if i == 1:
		prnt.append(arr[j - 1])
	else:
		prnt.append(arr[j - 1] - arr[i - 2])

for p in prnt:
	print(p)