import sys

number = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

student = list(range(1, number + 1))
order = []

for i in range(1, number + 1):
    order.insert(i - 1 - numbers[i - 1], student.pop(0))

print(' '.join(map(str, order)))