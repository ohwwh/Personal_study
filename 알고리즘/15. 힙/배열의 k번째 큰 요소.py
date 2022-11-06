import heapq
list1 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
list2 = [3, 2, 1, 5, 6, 4]


def findKthlargest(nums, k):
    nums.sort()
    nums = list(set(nums))[::-1]
    return nums[k - 1]

def findKthlargestheap(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, -n)
    for _ in range(k):
        heapq.heappop(heap)
    return -heapq.heappop(heap)
#대체 뭣하러 힙으로...?

#print(findKthlargest(list2, 2))
print(findKthlargestheap(list1, 4))
