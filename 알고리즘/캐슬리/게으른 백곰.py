N, K = map(int, input().split())

ice = []
idx = []

for _ in range(N):
	g, index = map(int, input().split())
	ice.append(g)
	idx.append(index)

max_index = max(idx)

arr = [0] * (max_index + 1)
for i in range(N):
	arr[idx[i]] = ice[i]

start = 0
end = 2 * K
sm = sum(arr[start:end])
mx = sm

while end < max_index:
	end += 1
	sm = sm - arr[start] + arr[end]
	start += 1
	if sm > mx:
		mx = sm

print(mx)