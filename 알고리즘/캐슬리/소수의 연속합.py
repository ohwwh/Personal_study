N = int(input())

arr = list(range(0, N + 1))
parr = []
n = 0

if N == 1:
	print(0)
	exit()

for p in arr[2:]:
	if arr[p] != 0:
		parr.append(p)
		n += 1
		i = 2
		while p * i <= N:
			if arr[p * i] != 0:
				arr[p * i] = 0
			i += 1


start = 0
end = 0
sum = parr[start]
ret = 0

while end < n and start < n:
	if sum < N:
		end += 1
		if end < n:
			sum += parr[end]
	elif sum > N:
		sum -= parr[start]
		start += 1
	else:
		ret += 1
		end += 1
		if end < n:
			sum += parr[end]

print(ret)
