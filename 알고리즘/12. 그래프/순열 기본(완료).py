nums1 = [1, 3, 5]


def permute(nums):
    ret = []
    rlist = []

    def dfs(clist):
        if not clist:
            ret.append(rlist[:])
            return
        else:
            for n in clist:
                nlist = clist[:]
                nlist.remove(n)
                rlist.append(n)
                dfs(nlist)
                rlist.pop()

    dfs(nums)
    return ret


print(permute(nums1))




