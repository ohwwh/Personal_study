
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

'''def solution(rooms):
    answer = 0
    visited = [False for _ in range(len(rooms))]
    for i in range(len(rooms)):
        if visited[i] == False:
            answer += 1
            v = rooms[i] - 1
            visited[i] = True
            while (visited[v] == False):
                visited[v] = True
                v = rooms[v] - 1
    if (answer != 1):
        answer -=1
    return answer'''
	# 전체 방이 몇 개 그룹으로 분할되는지 확인하기만 하면 되는 문제. 너무 어렵게 생각했다
	# 그룹이란 연쇄적으로 열릴 수 있는 방의 집합을 의미한다

print(solution([10,8,1,5,3,2,9,4,7,6]))