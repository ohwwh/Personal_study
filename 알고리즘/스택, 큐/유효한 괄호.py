str1 = '['


def isValid(s: str) -> bool:
    stack = []
    s = list(s)
    ret = True
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) < 1 or stack.pop() != '(':
                ret = False
                break
        elif s[i] == '}':
            if len(stack) < 1 or stack.pop() != '{':
                ret = False
                break
        else:
            if len(stack) < 1 or stack.pop() != '[':
                ret = False
                break
    return ret



def isValid2(s: str) -> bool:
    stack = []
    table = {'(': ')', '{': '}', '[': ']'}
    s = list(s)
    ret = True
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        else:
            if len(stack) < 1 or s[i] != table[stack.pop()]:
                ret = False
                break
    if len(stack) > 0:
        ret = False

    return ret


print(isValid2(str1))
