numsex = [-1, 0, 1, 2, -1, -4]
numex = [-2, 0, 0, 2, 2]
numex2 = [-3, -4, -2, 0, 2, 2, -2, 1, -1, 2, 3, -1, -5, -4, -5, 1]
numex2sorted = [-5, -5, -4, -4, -3, -2, -2, -1, -1, 0, 1, 1, 2, 2, 2, 3]
numex3 = [0, 0, 0]


def threeSum(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()
    summation = 0

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while right > left:
            summation = nums[i] + nums[left] + nums[right]
            if summation > 0:
                right -= 1
                while right > left and nums[right + 1] == nums[right]:
                    right -= 1
            elif summation < 0:
                left += 1
                while right > left and nums[left - 1] == nums[left]:
                    left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                right -= 1
                left += 1
                while right > left and nums[right + 1] == nums[right]:
                    right -= 1
                while right > left and nums[left - 1] == nums[left]:
                    left += 1

    return result


print(threeSum(numex3))
