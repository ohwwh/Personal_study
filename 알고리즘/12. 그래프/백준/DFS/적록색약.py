import sys
import copy

n = int(sys.stdin.readline())
grid = [list(sys.stdin.readline()) for _ in range(n)]


def color(gridex):
    cnt = 0
    grid = copy.deepcopy(gridex)

    def dfs(i, j, c):
        if i < 0 or j < 0 or j >= n or i >= n or grid[i][j] == 'P' or grid[i][j] != c:
            return False
        else:
            temp = grid[i][j]
            grid[i][j] = "P"
            dfs(i + 1, j, temp)
            dfs(i - 1, j, temp)
            dfs(i, j + 1, temp)
            dfs(i, j - 1, temp)
            return True

    for i in range(n):
        for j in range(n):
            if dfs(i, j, grid[i][j]):
                cnt += 1

    return cnt

def colorforblind(gridex):
    cnt = 0
    grid = copy.deepcopy(gridex)

    def dfs(i, j, c):
        if i < 0 or j < 0 or j >= n or i >= n or grid[i][j] == 'P':
            return False
        if grid[i][j] != c:
            if grid[i][j] == 'B':
                return False
            else:
                if c == 'B':
                    return False

        temp = grid[i][j]
        grid[i][j] = "P"
        dfs(i + 1, j, temp)
        dfs(i - 1, j, temp)
        dfs(i, j + 1, temp)
        dfs(i, j - 1, temp)
        return True

    for i in range(n):
        for j in range(n):
            if dfs(i, j, grid[i][j]):
                cnt += 1

    return cnt

print(color(grid))
print(colorforblind(grid))
