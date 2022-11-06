n = int(input())
seat = input()

p = 0

seat = seat.replace('LL', 'C')

def smaller(x, y):
    if x < y:
        return x
    else:
        return y

print(smaller(len(seat) + 1, n))