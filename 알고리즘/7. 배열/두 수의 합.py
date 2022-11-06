import math
import time
start = time.time()

nums = [2, 7, 11, 15]
nums = list(map(int, input().split()))
target = int(input())

'''nums2 = [i for i in nums if i <= target]

for i in nums2:
    if target - i in nums2:
        print([nums.index(i), nums.index(target-i)])
        break'''




'''nums2_map = {}
for i in range(len(nums)):
    if nums[i] <= target:
        nums2_map[nums[i]] = i

for i in list(nums2_map.keys()):
    if target - i in list(nums2_map.keys()):
        print([nums2_map[i], nums2_map[target-i]])
        break'''




'''for i, n in enumerate(nums):
    complement = target - n

    if complement in nums[i+1:]:
        print([nums.index(n), nums[i+1:].index(complement)+(i+1)])
        break'''



nums_map = {}
for i, num in enumerate(nums):
    nums_map[num] = i

for i, num in enumerate(nums):
    if target - num in nums_map and i != nums_map[target - num]:
        print([nums.index(num), nums_map[target - num]])
        break

end = time.time()
print(f"{end - start:.5f}sec")


