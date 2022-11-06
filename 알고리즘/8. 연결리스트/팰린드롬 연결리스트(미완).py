from collections import deque


linkedlist = [1, 2, 2, 1]


def isPalindrome(nums: list[int]) -> bool:
    deq = deque()
    ret = True
    if len(nums) % 2 == 1:
        start = len(nums) // 2 + 1
    else:
        start = len(nums) // 2

    for i in range(len(nums) // 2):
        deq.append(nums[i])
    for i in range(start, len(nums)):
        if nums[i] != deq.pop():
            ret = False
            break
    return ret


def isPalindrome2(nums: list[int]) -> bool:
    deq = deque()
    ret = True

    for i in range(len(nums)):
        deq.append(nums[i])
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            ret = False
            break
    return ret


print(isPalindrome(linkedlist))
print(isPalindrome2(linkedlist))
