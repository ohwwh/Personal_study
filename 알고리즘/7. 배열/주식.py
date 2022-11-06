stock1 = [7, 1, 5, 3, 6, 4]
stock2 = [7, 5, 3, 8, 1, 4]


def maxProfit(nums: list[int]) -> int:
    low = nums[0]
    maxP = 0
    for i in range(1, len(nums)):
        low = min(low, nums[i-1])
        maxP = max(maxP, nums[i] - low)

    return maxP


print(maxProfit(stock2))


