nums1 = [1, 2, 3, 4, 5]
nums2 = [i for i in range(1, 6)]


def combine(nums, l, n):
    ret = []
    rlist = []
    cnt = 0
    nums = [i for i in range(1, l+1)]
    l = len(nums)


    def dfs(clist, cnt, len):
        if cnt == n:
            ret.append(rlist[:])
            return
        elif not clist:
            return
        else:
            for i in range(len):
                nlist = clist[i+1:]
                rlist.append(clist[i])
                dfs(nlist, cnt+1, len-i-1)
                if rlist:
                    rlist.pop()


    dfs(nums, cnt, l)
    return ret


print(combine(nums2, 2))
