import heapq

heap = []
retarr = []
N = int(input())
number = 0
for _ in range(N):
	x = int(input())
	if x == 0 and number != 0:
		ret = heapq.heappop(heap)
		retarr.append(ret[1])
		number -= 1
	elif x == 0 and number == 0:
		retarr.append(0)
	else:
		heapq.heappush(heap, (abs(x), x))
		number += 1

for e in retarr:
	print(e)