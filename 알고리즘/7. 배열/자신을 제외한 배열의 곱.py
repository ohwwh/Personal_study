array = [1, 2, 3, 4]


def productExceptSelfBruteforce(nums: list[int]) -> list[int]:
    ret = []
    for i in range(len(nums)):
        eret = 1
        for j in range(len(nums)):
            if i == j:
                continue
            eret *= nums[j]

        ret.append(eret)

    return ret


def productExceptSelfTwoPointer(nums: list[int]) -> list[int]:
    out = []
    leftp = 1
    rightp = 1
    for i in range(len(nums)):
        out.append(leftp)
        leftp *= nums[i]
    for i in range(len(nums)):
        out[len(nums) - 1 - i] *= rightp
        rightp *= nums[len(nums) - 1 - i]

    return out


print(productExceptSelfTwoPointer(array))