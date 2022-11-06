from collections import defaultdict
import math
from re import I

f = math.inf
graph_org ={'A':{'B': 10, 'C':30, 'D':15}, 'B':{'E':20}, 'C':{'F':5}, 'D':{'C':5, 'F':20}, 'E':{'F':20}, 'F':{} }
graph =[[0,10,30,15,f,f],[f,0,f,f,20,f],[f,f,0,f,f,5],[f,f,5,0,f,20],[f,f,f,f,0,20],[f,f,f,f,f,0]]
visited = [False] * 6
cost = [f] * 7

#다익스트라는 딕셔너리 보다는 2차원 배열로 하는게 속이 편하다

def shortest(cost, n):
	min = n
	i = 0
	for i in range(n):
		if visited[i] == False and (cost[i] != f and cost[i] < cost[min]):
			min = i
	return min


def Dj(start, n):
	cost[start] = 0
	for _ in range(n):
		i = shortest(cost, n)
		visited[i] = True
		for j in range(n):
			if graph[i][j] != f and cost[j] > cost[i] + graph[i][j]:
				cost[j] = cost[i] + graph[i][j]

Dj(0, 6)
print(cost)