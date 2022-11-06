N, M = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(N - 1):
	arr[i + 1] = arr[i + 1] + arr[i]

n = 0
m = 0
narr = [0] * M
for i in range(N):
	for j in range(M):
		if arr[i] % M == j:
			narr[j] += 1

ret = 0

for i in range(M):
	if narr[i] != 0 or narr[i] != 1:
		ret += int(narr[i] * (narr[i] - 1) / 2)

ret += narr[0]

print(ret)