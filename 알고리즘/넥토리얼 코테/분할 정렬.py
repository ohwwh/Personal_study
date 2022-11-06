import itertools
import copy

def comb(arr, n):
	result = []
	if n == 0:
		return ([[]])
	for i in range(len(arr)):
		elem = arr[i]
		for rest in comb(arr[i + 1:], n - 1):
			result.append([elem] + rest)
	return result

def isRight(arr, n):
	l = len(arr)
	post = list(comb(list(range(1, l)), n - 1))
	for e in post:
		mx = -1
		for i in range(n):
			if i == 0:
				f = 0
			else:
				f = e[i - 1]
			if i == n - 1:
				if mx > min(arr[f:]):
					break
				else:
					return True
			else:
				if mx > min(arr[f:e[i]]):
					break
				else:
					mx = max(arr[f:e[i]])
			
def findMaxGroupCount(arr):
	l = len(arr)
	for i in range(l, 0, -1):
		if isRight(arr, i) == True:
			return i

print(findMaxGroupCount([4,2,10,5,9]))