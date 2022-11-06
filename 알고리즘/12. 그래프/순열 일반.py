nums1 = [1, 3, 5, 7, 9]


def permute(nums, n):
    ret = []
    rlist = []

    def dfs(clist):
        if len(clist) <= len(nums) - n:
            ret.append(rlist[:])
            return
        else:
            for e in clist:
                nlist = clist[:]
                nlist.remove(e)
                rlist.append(e)
                dfs(nlist)
                rlist.pop()

    dfs(nums)
    return ret


print(permute(nums1, 2))