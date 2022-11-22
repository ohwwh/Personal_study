import copy
import sys
sys.setrecursionlimit(15000)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ddx = [1,-1,0,0,1,1,-1,-1]
ddy = [0,0,1,-1,1,-1,1,-1]

def dfs(x, y, w, h, image):
	image[y][x] = -1
	for i in range(4):
		u = x + dx[i]
		v = y + dy[i]
		if u >= 0 and u < w and v >= 0 and v < h:
			if image[v][u] == 1:
				dfs(u, v, w, h, image)

def dfs2(x, y, w, h, image2):
	image2[y][x] = -1
	for i in range(8):
		u = x + ddx[i]
		v = y + ddy[i]
		if u >= 0 and u < w and v >= 0 and v < h:
			if image2[v][u] == 1:
				dfs2(u, v, w, h, image2)

def solution(image):
	h = len(image)
	w = len(image[0])
	image2 = copy.deepcopy(image)
	answer = 0
	answer2 = 0
	for i in range(h):
		for j in range(w):
			if image[i][j] == 1:
				dfs(j, i, w, h, image)
				answer += 1
			if image2[i][j] == 1:
				dfs2(j, i, w, h, image2)
				answer2 += 1
	ret = [answer, answer2]
	return ret

image = [[1,1,0,1,1],[0,1,0,1,1],[1,0,0,0,1],[1,1,0,1,0]]

print(solution(image))