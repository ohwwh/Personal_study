import sys

dwarf = [0 for i in range(9)]
for i in range (9):
    dwarf[i] = int(sys.stdin.readline())

sumd = sum(dwarf)
for i in range (9):
    for j in range (i + 1, 9):
        if sumd - dwarf[i] - dwarf[j] == 100:
            i, j = dwarf[i], dwarf[j]
            dwarf.remove(i)
            dwarf.remove(j)
            dwarf.sort()
            for k in dwarf:
                print(str(k))
            exit()