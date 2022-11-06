from collections import deque

N, L = map(int, input().split())

arr = list(map(int, input().split()))

q = deque()
for i in range(N):
    while q and q[-1][0] > arr[i]:
        q.pop()
    q.append((arr[i], i))
    while q and q[0][1] < i - L + 1:
        q.popleft()
    print(q[0][0], end=' ')


