from collections import deque

T = [73, 74, 75, 71, 69, 72, 76, 73]
T1 = [73, 74, 75, 71, 65, 63, 60, 61, 65, 67, 72, 70, 68, 76, 73]


def dailyTemperatures(t: list[int]) -> list[int]:
    output = [0]*len(t)
    deq = deque()
    for i in range(len(t)):
        while len(deq) > 0 and t[i] > t[deq[-1]]:
            pop = deq.pop()
            output[pop] = i - pop
        deq.append(i)

    return list(output)


print(dailyTemperatures(T1))




