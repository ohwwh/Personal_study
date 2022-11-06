code = input()
n = len(code)
r = 1

for i in range(2, int(n**(1/2)) + 1):
    if n % i == 0:
        r = i
c = int(n / r)

arr = [list(range(c)) for _ in range(r)]

for i in range(n):
    arr[i % r][int(i / r)] = code[i]

for c1 in arr:
    for c2 in c1:
        print(c2,end='')