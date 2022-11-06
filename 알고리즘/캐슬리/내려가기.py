from copy import deepcopy

N = int(input())

arr = []

for _ in range(N):
	iarr = list(map(int, input().split()))
	arr.append(iarr)

temp_max = deepcopy(arr[0])
temp_min = deepcopy(arr[0])
max_arr = [0] * 3
min_arr = [0] * 3

for i in range(1, N):
	max_arr[0] = max(temp_max[0] + arr[i][0], temp_max[1] + arr[i][0])
	max_arr[1] = max(temp_max[0] + arr[i][1], temp_max[1] + arr[i][1], temp_max[2] + arr[i][1])
	max_arr[2] = max(temp_max[1] + arr[i][2], temp_max[2] + arr[i][2])
	temp_max[0] = max_arr[0]
	temp_max[1] = max_arr[1]
	temp_max[2] = max_arr[2]

for i in range(1, N):
	min_arr[0] = min(arr[i][0] + temp_min[0], arr[i][0] + temp_min[1])
	min_arr[1] = min(arr[i][1] + temp_min[0], arr[i][1] + temp_min[1], arr[i][1] + temp_min[2])
	min_arr[2] = min(arr[i][1] + temp_min[2], arr[i][2] + temp_min[1])
	temp_min[0] = min_arr[0]
	temp_min[1] = min_arr[1]
	temp_min[2] = min_arr[2]

print(max(temp_max), end=' ')
print(min(temp_min))