import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]


def prequent(s: str, b: list):
    words = [s for s in re.sub('[^\w]', ' ', s).lower().split() if s not in b]
    return words


words = prequent(paragraph, banned)

counts = collections.defaultdict(int)
for word in words:
    counts[word] += 1

ret = max(counts, key=counts.get)
print('{0} , {1}'.format(ret, counts[ret]))
print('%s , %d'%(ret, counts[ret]))









