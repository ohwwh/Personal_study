import sys

sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())

arrN = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

arrM = list(map(int, sys.stdin.readline().split()))

arrN.sort()
#arrM.sort()

def find_by_index(n, i1, i2, arr):
	while i1 <= i2:
		i3 = (i1 + i2) // 2
		if arr[i3] == n:
			return 1
		elif arr[i3] > n:
			i2 = i3 - 1
		elif arr[i3] < n:
			i1 = i3 + 1
	return 0

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(M):
	print(find_by_index(arrM[i], 0, N - 1, arrN), end=' ')