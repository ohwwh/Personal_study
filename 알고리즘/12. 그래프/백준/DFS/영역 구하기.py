import sys
sys.setrecursionlimit(1000000000)

m, n, k = map(int, sys.stdin.readline().split())

nums = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
grid = [[0] * n for _ in range(m)]

for s in range(k):
    for i in range(m - nums[s][3], m - nums[s][1]):
        for j in range(nums[s][0], nums[s][2]):
            if grid[i][j] != 1:
                grid[i][j] = 1

ar = [0]
def area(i, j):
    if i < 0 or j < 0 or i >= n or j >= m or grid[j][i] != 0:
        return False
    else:
        grid[j][i] = 1
        ar[0] += 1
        area(i+1, j)
        area(i - 1, j)
        area(i, j+1)
        area(i, j-1)
        return True


ret = []
cnt = 0
for i in range(n):
    for j in range(m):
        if grid[j][i] == 0 and area(i, j):
            ret.append(ar[0])
            ar[0] = 0
            cnt += 1

ret.sort()
print(cnt)
for i in ret:
    print(i, end=" ")