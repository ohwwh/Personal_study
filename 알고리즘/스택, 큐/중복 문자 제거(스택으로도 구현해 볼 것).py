import collections

str1 = 'bcabc'
str2 = 'cbacdcbc'
str3 = 'ebcabc'
str4 = 'ebcabce'


def removeDupRecursive(s: str) -> str:

    newlist = []

    def suffix(s: str):
        if len(s) == 0:
            return ''
        else:
            sortedset = sorted(set(s))
            for char in sortedset:
                if set(s[s.index(char):]) == set(s):
                    newlist.append(char)
                    suffix(s[s.index(char):].replace(char, ''))
                    break
                else:
                    continue
    suffix(s)
    return ''.join(newlist)


def removeDupStack(s: str) -> str:
    stack = []
    countdic = collections.Counter(s)
    inclusion = set()
    for i in range(len(s)):
        if s[i] not in inclusion:
            while len(stack) > 0 and s[i] <= stack[-1] and countdic[stack[-1]] > 0:
                inclusion.remove(stack.pop())
            stack.append(s[i])
            countdic[s[i]] -= 1
            inclusion.add(s[i])

    return ''.join(stack)


print(removeDupStack(str1))
print(removeDupStack(str2))
print(removeDupStack(str3))
print(removeDupStack(str4))












