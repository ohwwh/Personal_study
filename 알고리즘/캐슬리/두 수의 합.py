n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

number = 0
start = 0
end = n - 1

while end < n and start < end:
	if arr[start] + arr[end] == x:
		number += 1
		start += 1
		end -= 1
	elif arr[start] + arr[end] < x:
		start += 1
	else:
		end -= 1

print(number)