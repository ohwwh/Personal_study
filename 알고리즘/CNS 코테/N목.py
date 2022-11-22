

def solution(arr, w, h, k):
	new_arr = []
	for e in arr:
		new_arr.append(list(map(int, list(e[0]))))
	
	answer = 0

	if w < k or h < k:
		return 0

	for j in range(h):
		for i in range(w):
			if new_arr[j][i] != 0 and new_arr[j][i] & 2 != 2:
				if (i == 0 or new_arr[j][i - 1] == 0) and (i + k == w or (i + k < w and new_arr[j][i + k] == 0)):
					l = 0
					flag = 0
					for l in range(k):
						if i + l >= w or new_arr[j][i + l] == 0:
							flag = 1
							break
						else:
							new_arr[j][i + l] |= 2
						l += 1
					if flag != 1:
						answer += 1

			if new_arr[j][i] != 0 and new_arr[j][i] & 4 != 4:
				if (j == 0 or new_arr[j - 1][i] == 0) and (j + k == h or (j + k < h and new_arr[j + k][i] == 0)):
					l = 0
					flag = 0
					for l in range(k):
						if j + l >= h or new_arr[j + l][i] == 0:
							flag = 1
							break 
						else:
							new_arr[j + l][i] |= 4
						l += 1
					if flag != 1:
						answer += 1
			
			if new_arr[j][i] != 0 and new_arr[j][i] & 8 != 8:
				if (i == 0 or j == 0 or new_arr[j - 1][i - 1] == 0) and (j + k == h or i + k == w or (j + k < h and i + k < w and new_arr[j + k][i + k] == 0)):
					l = 0
					flag = 0
					for l in range(k):
						if i + l >= w or j + l >= h or new_arr[j + l][i + l] == 0:
							flag = 1
							break
						else:
							new_arr[j + l][i + l] |= 8
						l += 1
					if flag != 1:
						answer += 1
			
			if new_arr[j][i] != 0 and new_arr[j][i] & 16 != 16:
				if (i == w - 1 or j == 0 or new_arr[j - 1][i + 1] == 0) and (j + k == h or i - k == -1 or (j + k < h and i - k >= 0 and new_arr[j + k][i - k] == 0)):
					l = 0
					flag = 0
					for l in range(k):
						if i - l < 0 or j + l >= h or new_arr[j + l][i - l] == 0:
							flag = 1
							break
						else:
							new_arr[j + l][i - l] |= 16
						l += 1
					if flag != 1:
						answer += 1

	return answer
				
	



arr = [
	["011110001"],
	["000000011"],
	["111100011"],
	["111110011"],
	["111110011"],
	["111100000"],
	["000100000"],
]

print(solution(arr, 9, 7, 4))

