import sys
import collections

width, height = map(int, sys.stdin.readline().split())
n = int(input())
store = collections.defaultdict(list)
length = (width + height) * 2
ret = 0

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[0] == 1:
        temp[1] = width - temp[1]
    elif temp[0] == 4:
        temp[1] = height - temp[1]
    store[temp[0]].append(temp[1])

guard = list(map(int, sys.stdin.readline().split()))
if guard[0] == 1:
    guard[1] = width - guard[1]
elif guard[0] == 4:
    guard[1] = height - guard[1]

def mklst(start):
    if start == 2:
        return [2, 3, 1, 4]
    elif start == 3:
        return [3, 1, 4, 2]
    elif start == 1:
        return [1, 4, 2, 3]
    else:
        return [4, 2, 3, 1]

def smaller(x, y):
    if x < y:
        return x
    else:
        return y

lst = mklst(guard[0])
path = guard[1]


if guard[0] == 1 or guard[0] == 2:
    for i in range(4):
        if i != 0 and i % 2 == 1:
            path += height
        elif i != 0 and i % 2 == 0:
            path += width
        for j in store[lst[i]]:
            ret += smaller(abs(path - j), length - abs(path - j))
else:
    for i in range(4):
        if i != 0 and i % 2 == 0:
            path += height
        elif i != 0 and i % 2 == 1:
            path += width
        for j in store[lst[i]]:
            ret += smaller(abs(path - j), length - abs(path - j))

print(ret)