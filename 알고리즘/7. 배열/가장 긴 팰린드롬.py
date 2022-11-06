
print('문자열을 입력하시오: ')
s = input()


def longestPalindrome(s: str):
    result = ''

    def expand(left, right):
        if right > len(s)-1:
            return ''
        else:
            if s[left] == s[right]:
                while s[left] == s[right] and left >= 0 and right < len(s):
                    left -= 1
                    right += 1
                return s[left+1:right]
            else:
                return ''

    if len(s) < 2 or s == s[::-1]:
        return s
    else:
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result


print(longestPalindrome(s))

