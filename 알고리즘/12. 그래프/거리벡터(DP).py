import math
from itertools import permutations
from copy import deepcopy

f = math.inf

'''graph_org ={'A':{'B': 10, 'C':30, 'D':15}, 'B':{'E':20}, 'C':{'F':5}, 'D':{'C':5, 'F':20}, 'E':{'F':20}, 'F':{} }
graph =[[0,10,30,15,f,f],[f,0,f,f,20,f],[f,f,0,f,f,5],[f,f,5,0,f,20],[f,f,f,f,0,20],[f,f,f,f,f,0]]'''
graph_org ={'A':{'B': 4, 'C':50}, 'B':{'C':1}, 'C':{}}
'''graph =[[0,4,50],[4,0,1],[50,1,0]]
cost =[[[0,4,50],[f,f,f],[f,f,f]],[[f,f,f],[4,0,1],[f,f,f]],[[f,f,f],[f,f,f],[50,1,0]]]'''
graph =[[0,10,30,15,f,f],[10,0,f,f,20,f],[30,f,0,5,f,5],[15,f,5,0,f,20],[f,20,f,f,0,20],[f,f,5,20,20,0]]
cost = [[[0,10,30,15,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f]],
[[f,f,f,f,f,f],[10,0,f,f,20,f],[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f]],
[[f,f,f,f,f,f],[f,f,f,f,f,f],[30,f,0,5,f,5],[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f]],
[[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f],[15,f,5,0,f,20],[f,f,f,f,f,f],[f,f,f,f,f,f]],
[[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f],[f,20,f,f,0,20],[f,f,f,f,f,f]],
[[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,5,20,20,0]]]

n = 6

def broadcast(cost, n):
	for i in range(n):
		for u in range(n):
			if graph[i][u] != f and u != i:
				cost[u][i] = deepcopy(cost[i][i])

def update_cost(x, y, cost, n):
	min = f
	for u in range(n):
		if graph[x][u] != f and u != x:
			nc = graph[x][u] + cost[x][u][y]
			if nc < min:
				min = nc
	if cost[x][x][y] == min:
		return False
	else:
		cost[x][x][y] = min
		return True

def update_cost_poisoned(x, y, cost, n):
	min = f
	for u in range(n):
		if graph[x][u] != f and u != x:
			nc = graph[x][u] + cost[x][u][y]
			if nc < min:
				min = nc
	if cost[x][x][y] == min:
		return False
	else:
		cost[x][x][y] = min
		return True

path = list(permutations(range(n), 2))

def process(path, cost, n):
	round = 0
	while True:
		round += 1
		flag = True
		for p in path:
			broadcast(cost, n)
			t = update_cost(p[0], p[1], cost, n)
			if t is True:
				flag = False
		if flag is True:
			break
	return round

round = process(path, cost, n)
print(round)
graph = [[0,50,50],[50,0,1],[50,1,0]]
round = process(path, cost, n)
print(round)