import sys

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        for l in range(1, 3):
            if arr[i][j] == l:
                if j + 4 < 19:
                    for k in range(1, 5):
                        if arr[i][j + k] != l:
                            k -= 1
                            break
                    if k == 4:
                        if j + k == 18 or (j + k < 18 and arr[i][j + 5] != l):
                            if j == 0 or (j > 0 and arr[i][j - 1] != l):
                                print(l)
                                print(i+1, j+1)
                                exit()
                if i + 4 < 19:
                    for k in range(1, 5):
                        if arr[i + k][j] != l:
                            k -= 1
                            break
                    if k == 4:
                        if  i + k == 18 or (i + k < 18 and arr[i + 5][j] != l):
                            if i == 0 or (i > 0 and arr[i - 1][j] != l):
                                print(l)
                                print(i+1, j+1)
                                exit()
                    if j + 4 < 19:
                        for k in range(1, 5):
                            if arr[i + k][j + k] != l:
                                k -= 1
                                break
                        if k == 4:
                            if (i + k == 18 or j + k == 18) or (i + k < 18 and j + k < 18 and arr[i + 5][j + 5] != l):
                                if (i == 0 or j == 0) or (i > 0 and j > 0 and arr[i - 1][j - 1] != l):
                                    print(l)
                                    print(i+1, j+1)
                                    exit()
                    if j > 3:
                        for k in range(1, 5):
                            if arr[i + k][j - k] != l:
                                k -= 1
                                break
                        if k == 4:
                            if (i + k == 18 or j == 4) or (i + k < 18 and j > 4 and arr[i + 5][j - 5] != l):
                                if (i == 0 or j == 18) or (i > 0 and j < 18 and arr[i - 1][j + 1] != l):
                                    print(l)
                                    print(i+5, j-3)
                                    exit()


print(0)