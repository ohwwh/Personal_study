N, M = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = 0
ret = 0

sum = arr[0]
while end < N:
	if sum < M:
		end += 1
		if end < N:
			sum += arr[end]
	elif sum > M:
		if start == end:
			end += 1
			if end < N:
				sum += arr[end]
		sum -= arr[start]
		start += 1
	else:
		ret += 1
		sum -= arr[start]
		start += 1

print(ret)
