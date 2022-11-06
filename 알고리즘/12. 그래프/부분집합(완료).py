nums1 = [1, 2, 3]

def subset(nums):
    ret = []
    rlist = []
    l = len(nums)

    def dfs(clist, len):
        if not clist:
            ret.append(rlist[:])
            return
        else:
            for i in range(len+1):
                nlist = clist[i+1:]
                if i < len:
                    rlist.append(clist[i])
                dfs(nlist, len-i-1)
                if i < len:
                    rlist.pop()

    dfs(nums, l)
    return ret


def subset2(nums):
    ret = []
    rlist = []
    l = len(nums)

    def dfs(clist, len):
        ret.append(clist)
        for i in range(len, l):
            dfs(clist + [nums[i]], i+1)

    dfs([], 0)
    return ret



print(subset2(nums1))




