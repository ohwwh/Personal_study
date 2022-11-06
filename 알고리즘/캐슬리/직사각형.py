import sys

lst1 = list(map(int, sys.stdin.readline().split()))
lst2 = list(map(int, sys.stdin.readline().split()))
lst3 = list(map(int, sys.stdin.readline().split()))
lst4 = list(map(int, sys.stdin.readline().split()))


def type(lst):
    if lst[4] > lst[2] or lst[5] > lst[3] or lst[6] < lst[0] or lst[7] < lst[1]:
        return 'd'
    elif (lst[4] == lst[2] or lst[6] == lst[0]) and (lst[5] == lst[3] or lst[7] == lst[1]):
        return 'c'
    elif lst[4] == lst[2] or lst[5] == lst[3] or lst[6] == lst[0] or lst[7] == lst[1]:
        return 'b'
    else:
        return 'a'



print(type(lst1))
print(type(lst2))
print(type(lst3))
print(type(lst4))
