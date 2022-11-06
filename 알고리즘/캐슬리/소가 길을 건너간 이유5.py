N, K, B = map(int, input().split())

sign = list(range(1, N + 1))
for _ in range(B):
	idx = int(input())
	sign[idx - 1] = 0

start = 0
end = K - 1
to_fix = 0

for i in range(start, end + 1):
	if sign[i] == 0:
		to_fix += 1

min = to_fix

for _ in range(N - K):
	if sign[start] == 0:
		to_fix -= 1
	if end < N - 1 and sign[end + 1] == 0:
		to_fix += 1
	start += 1
	end += 1
	if to_fix < min:
		min = to_fix
	
print(min)