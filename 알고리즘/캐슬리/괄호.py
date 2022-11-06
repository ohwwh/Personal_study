import sys

t = int(input())
pars = [sys.stdin.readline() for _ in range(t)]

def isValid(par):
    buf = []
    i = 0
    while par[i] != '\n':
        if par[i] == '(':
            buf.append('(')
        else:
            if len(buf) == 0:
                return "NO"
            buf.pop()
        i += 1
    if len(buf) == 0:
        return "YES"
    else:
        return "NO"

for i in range(t):
    print(isValid(pars[i]))