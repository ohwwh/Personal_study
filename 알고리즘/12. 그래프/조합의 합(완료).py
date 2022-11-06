nums1 = [2, 3, 5]
target1 = 8


def combine(nums, target):
    ret = []
    rlist = []
    l = len(nums)
    sum = 0

    def dfs(clist, len, sum):
        if sum == target:
            ret.append(rlist[:])
            return
        elif sum > target:
            return
        else:
            for i in range(len):
                nlist = clist[i:]
                rlist.append(clist[i])
                dfs(nlist, len - i, sum + clist[i])
                if rlist:
                    rlist.pop()

    dfs(nums, l, sum)
    return ret


print(combine(nums1, target1))
