
from collections import deque
from itertools import combinations

def can_open(v, n, rooms):
	open_num = 0
	vlen = 0
	open = [0] * n
	for i in v:
		open[i] = 1
		open_num += 1
		vlen += 1
	master = open_num
	while v:
		k = v.pop()
		vlen -= 1
		if open[rooms[k] - 1] == 0:
			open[rooms[k] - 1] = 1
			open_num += 1
			v.append(rooms[k] - 1)
			vlen += 1
		elif vlen == 0:
			if open_num + 1 == n:
				return master
	if open_num == n:
		return master
	else:
		return -1

def solution(rooms):
	n = len(rooms)
	idx_lst = [0] * n
	for i in range(n):
		idx_lst[i] = i
	unprocessed = list(map(list, combinations(idx_lst, 1)))
	for k in range(2, n + 1):
		while unprocessed:
			v = unprocessed.pop()
			ret = can_open(v, n, rooms)
			if ret != -1:
				if ret != -2:
					return (ret)
		unprocessed = list(map(list, combinations(idx_lst, k)))
	return n

print(solution([1,2,3,4,5,6]))