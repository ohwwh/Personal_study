from itertools import combinations
from unittest.result import failfast

def get_score(str, set):
    isshift = 0
    score = 0
    if 'shift' in set:
        isshift = 1
    for i in str:
        if i != ' ':
            if i.isupper():
                if isshift == 0 or i.lower() not in set:
                    return (0)
            else:
                if i not in set:
                    return (0)
        if i.isupper() and i.lower() in set and isshift == 1:
            score += 2
        else:
            score += 1
    return score


def solution(sen, n):
    isshift = 0
    char_set = set()
    comb = []
    for str in sen:
        if str.islower() == False:
            isshift = 1
            str = str.lower()
        char_set = char_set | set(str)
    if isshift == 1:
        char_set.add('shift')
    char_set.remove(' ')
    max = 0
    for i in range(1, n + 1):
        comb += list(combinations(char_set, i))
    for st in comb:
        s = 0
        for str in sen:
            s += get_score(str, st)
        if s > max:
            max = s
    return max

sen = ["ABcD", "bdbc", "a", "Line neWs"]
s = solution(sen, 7)
print(s)