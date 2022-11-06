import sys
sys.setrecursionlimit(1000000)

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

result = 0
ret = set()

def dfs(x, y, idx, result):
	result = result * 10 + arr[y][x]
	if idx == 5:
		ret.add(result)
		return
	for i in range(4):
		if (x + dx[i] < 5 and x + dx[i] >= 0 and y + dy[i] < 5 and y + dy[i] >= 0):
			dfs(x + dx[i], y + dy[i], idx + 1, result)

for i in range(5):
	for j in range(5):
		dfs(i, j, 0, 0)

print(len(ret))