import sys

bingo = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]
processed = []

bingo_num = 0

def isbingo(bingo, k, l):
    ret = 4

    for i in range (5):
        if bingo[i][l] != 0:
            ret -= 1
            break
    for i in range(5):
            if bingo[k][i] != 0:
                ret -= 1
                break
    if k == l:
        for i in range (5):
            if bingo[i][i] != 0:
                ret -= 1
                break
    else:
        ret -= 1
    if k + l == 4:
        for i in range (5):
            if bingo[i][4 - i] != 0:
                ret -= 1
                break
    else:
        ret -= 1
    return ret

for i in range (5):
    for j in range (5):
        for k in range (5):
            if bingo[k].count(call[i][j]) != 0:
                l = bingo[k].index(call[i][j])
                processed.append((k, l))
                bingo[k][l] = 0
                bingo_num += isbingo(bingo, k, l)
                if bingo_num >= 3:
                    print((5 * i) + j + 1)
                    exit()
                break
