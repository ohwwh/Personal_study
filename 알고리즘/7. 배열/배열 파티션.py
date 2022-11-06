array1 = [1, 4, 3, 2, 9, 8, 6]
array1sorted = [1, 2, 3, 4, 6, 8, 9]
array2 = [1, 4, 3, 2]


def arrayPartition(nums: list[int]) -> int:
    nums.sort()
    ret = sum(nums[0:-1:2])
    if len(nums) % 2 == 1:
        ret += nums[-1]
    return ret


print(arrayPartition(array2))





