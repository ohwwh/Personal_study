import sys

width = []
width_index = []
height = []
height_index = []
dir = []
size = []
width_sum = 0
height_sum = 0

number = int(input())
for i in range (6):
    tmp = tuple(map(int, sys.stdin.readline().split()))
    if tmp[0] == 4 or tmp[0] == 3:
        dir.append(tmp[0])
        size.append(tmp[1])
        width_sum += tmp[0]
        height.append(tmp[1])
        height_index.append(i)
    else:
        dir.append(tmp[0])
        size.append(tmp[1])
        height_sum += tmp[0]
        width.append(tmp[1])
        width_index.append(i)

maxw = max(width)
maxh = max(height)
outer = maxw * maxh
i = width_index[width.index(maxw)]
j = height_index[height.index(maxh)]
inner = abs(size[(i - 1) % 6] - size[(i + 1) % 6]) * abs(size[(j - 1) % 6] - size[(j + 1) % 6])

print((outer - inner) * number)